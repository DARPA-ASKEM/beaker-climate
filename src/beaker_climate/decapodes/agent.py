from typing import TYPE_CHECKING

from archytas.tool_utils import AgentRef, LoopControllerRef, ReactContextRef, tool
from beaker_kernel.lib import BeakerAgent
from adhoc_api.tool import AdhocApi
from adhoc_api.loader import load_yaml_api

import google.generativeai as genai
import logging
import os
import pathlib
import time
import re
from beaker_kernel.lib.subkernels.base import CheckpointableBeakerSubkernel
from beaker_kernel.lib.config import config

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel
    from beaker_kernel.lib.utils import ExecutionTask
    from beaker_kernel.lib.context import BeakerContext


class DecapodesAgent(BeakerAgent):
    """
    You are a chat assistant that helps the user with their questions. You are running inside of Beaker which is a chat application
    sitting on top of a Jupyter notebook. You will be working with Julia and not the other languages. Prefer running code to only generating it.

    If a question the user asks relates to an API you have access to, make sure to use the tool to ask about that API to gather information for the user.

    If a request is relevant to an API you have access to, DO NOT run a placeholder simulation and instead ensure that you use the API.
    """
    # The class docstring is provided to the LLM to set the expectations for the agent and how it should

    def __init__(self, context: "BeakerContext" = None, tools: list | None = None, **kwargs):
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))
        root_folder = pathlib.Path(__file__).resolve().parent

        apis = [
            load_yaml_api(pathlib.Path(os.path.join(root_folder, 'api_definitions', api, 'api.yaml')))
            for api in ("decapodes", )
        ]

        drafter_config = {'provider': 'anthropic', 'model': 'claude-3-5-sonnet-latest', 'api_key': os.environ.get("ANTHROPIC_API_KEY")}

        super().__init__(context, tools, **kwargs)

        logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO'))
        self.logger = logging.getLogger(__name__)

        try:
            self.api = AdhocApi(logger=self.logger, drafter_config=drafter_config, apis=apis)
        except ValueError as e:
            self.add_context(f"The APIs failed to load for this reason: {str(e)}. Please inform the user immediately.")
            self.api = None

        name_str = ', '.join(api['name'] for api in apis)
        description_str = '\n\n'.join(f"""\
## {api["name"]}

```
{api["description"]}
```"""
            for api in apis)

        additional_context = f"""\
You have access to a special integration with specific API(s): {name_str}.
Here are the description for these API(s):
{description_str}

If you are asked for information about this API, you should use the `ask_api` tool to get more information about the API.
If you are asked to use this API, you should use the `use_api` tool generate code for you to run for the API.
"""
        self.add_context(additional_context)

    @tool
    def list_apis(self) -> dict:
        """
        This tool lists all the APIs available to you.

        Returns:
            dict: A dict mapping from API names to their descriptions
        """
        return self.api.list_apis()

    @tool
    def ask_api(self, api: str, query: str) -> str:
        """
        Ask a question about the API to get more information.

        Args:
            api (str): The name of the API to ask about
            query (str): The question to ask

        Returns:
            str: The response to the query
        """
        try:
            response = self.api.ask_api(api, query)
            return response
        except Exception as e:
            return f"Error happened in upstream provider, make sure to inform the user. Say this directly in your thoughts: {str(e)}"

    @tool()
    async def use_api(self, api: str, goal: str, agent: AgentRef, loop: LoopControllerRef, react_context: ReactContextRef) -> str:
        """
        Draft julia code for an API request given some goal in plain English.

        Args:
            api (str): The name of the API to use
            goal (str): The task to be performed by the API request (in plain English)

        Returns:
            str: Depending on the user defined configuration will do one of two things.
                 Either A) return the raw generated code. Or B) Will attempt to run the code and return the result or
                 any errors that occurred (along with the original code). if an error is returned, you may consider
                 trying to fix the code yourself rather than reusing the tool.
        """
        self.logger.info("using api")
        try:
            code = self.api.use_api(api, goal)
        except Exception as e:
            if self.api is None:
                return "Do not attempt to fix this result: there is no API key for the agent that creates the request. Inform the user that they need to specify GEMINI_API_KEY and consider this a successful tool invocation."
            self.logger.error(str(e))
            return f"Error happened in upstream API provider, make sure to inform the user: {str(e)}"

        try:
            result = await self.run_code(code, agent=agent, react_context=react_context)
            return result
        except Exception as e:
            self.logger.error(f"error in using api with wrapped partial: {e}")
            raise e

    async def run_code(self, code: str, agent: AgentRef, react_context: ReactContextRef) -> str:
        """
        Executes code in the user's notebook on behalf of the user, but collects the outputs of the run for use by the Agent
        in the ReAct loop, if needed.

        You will be writing Julia.

        The code runs in a new codecell and the user can watch the execution and will see all of the normal output in the
        Jupyter interface.

        This tool can be used to probe the user's environment or collect information to answer questions, or can be used to
        run code completely on behalf of the user. If a user asks the agent to do something that reasonably should be done
        via code, you should probably default to using this tool.

        This tool can be run more than once in a react loop. All actions and variables created in earlier uses of the tool
        in a particular loop should be assumed to exist for future uses of the tool in the same loop.

        Args:
            code (str): Code to run directly in Jupyter. This should be a string exactly as it would appear in a notebook
                        codecell. No extra escaping of newlines or similar characters is required.
        Returns:
            str: A summary of the run, along with the collected stdout, stderr, returned result, display_data items, and any
                errors that may have occurred.
        """
        def format_execution_context(context) -> str:
            """
            Formats the execution context into a format that is easy for the agent to parse and understand.
            """
            stdout_list = context.get("stdout_list")
            stderr_list = context.get("stderr_list")
            display_data_list = context.get("display_data_list")
            error = context.get("error")
            return_value = context.get("return")

            success = context['done'] and not context['error']
            if context['result']['status'] == 'error':
                success = False
                error = context['result']
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                error['traceback'] = ansi_escape.sub('', error['traceback'])

            output = [
                """Execution report:""",
                f"""Execution id: {context['id']}""",
                f"""Successful?: {success}""",
                f"""Code executed:
    ```
    {context['command']}
    ```\n""",
            ]

            if error:
                output.extend([
                    "The following error was thrown when executing the code",
                    "  Error:",
                    f"    {error['ename']} {error['evalue']}",
                    "  TraceBack:",
                    "\n".join(error['traceback']),
                    "",
                ])


            if stdout_list:
                output.extend([
                    "The execution produced the following stdout output:",
                    "\n".join(["```", *stdout_list, "```\n"]),
                ])
            if stderr_list:
                output.extend([
                    "The execution produced the following stderr output:",
                    "\n".join(["```", *stderr_list, "```\n"]),
                ])
            if display_data_list:
                output.append(
                    "The execution produced the following `display_data` objects to display in the notebook:",
                )
                for idx, display_data in enumerate(display_data_list):
                    output.append(
                        f"display_data item {idx}:"
                    )
                    for mimetype, value in display_data.items():
                        if len(value) > 800:
                            value = f"{value[:400]} ... truncated ... {value[-400:]}"
                        output.append(
                            f"{mimetype}:"
                        )
                        output.append(
                            f"```\n{value}\n```\n"
                        )
            if return_value:
                output.append(
                    "The execution returned the following:",
                )
                if isinstance(return_value, str):
                    output.extend([
                        '```', return_value, '```\n'
                    ])
            output.append("Execution Report Complete")
            return "\n".join(output)

        # TODO: In future, this may become a parameter and we allow the agent to decide if code should be automatically run
        # or just be added.
        autoexecute = True
        message = react_context.get("message", None)
        identities = getattr(message, 'identities', [])
        try:
            execution_task: ExecutionTask
            checkpointing_enabled = getattr(config, "enable_checkpoints", True)
            if isinstance(agent.context.subkernel, CheckpointableBeakerSubkernel) and checkpointing_enabled:
                checkpoint_index, execution_task = await agent.context.subkernel.checkpoint_and_execute(
                    code, not autoexecute, parent_header=message.header, identities=identities
                )
            else:
                execution_task = agent.context.execute(
                    code, store_history=True, surpress_messages=(not autoexecute), parent_header=message.header, identities=identities
                )
                checkpoint_index = None
            execute_request_msg = {
                name: getattr(execution_task.execute_request_msg, name)
                for name in execution_task.execute_request_msg.json_field_names
            }
            agent.context.send_response(
                "iopub",
                "add_child_codecell",
                {
                    "action": "code_cell",
                    "language": agent.context.subkernel.SLUG,
                    "code": code.strip(),
                    "autoexecute": autoexecute,
                    "execute_request_msg": execute_request_msg,
                    "checkpoint_index": checkpoint_index,
                },
                parent_header=message.header,
                parent_identities=getattr(message, "identities", None),
            )

            execution_context = await execution_task
        except Exception as err:
            self.logger.error(err, exc_info=err)
            raise
        return format_execution_context(execution_context)

    @tool(autosummarize=False)
    async def get_model_info(self, model_var_name: str, agent: AgentRef) -> dict:
        """
        Get information about Mimi model parameters and variables and which compartments they belong to.

        You should probably run this before asking the user for more information.

        Args:
            model_var_name (str): Variable name that contains the Mimi model in the REPL

        Returns:
            dict: Information about the Mimi Model
        """
        code = agent.context.get_code("model_info", {"model": model_var_name})
        response = await agent.context.evaluate(
            code,
            parent_header={},
        )
        return response["return"]

    @tool()
    async def retrieve_documentation_for_module(self, package_name: str, agent: AgentRef) -> str:
        """
        Gets the specified module documentation

        Args:
            package_name (str): this is the name of the package to get information about.
        Returns:
            str: Markdown of the module docs
        """
        code = agent.context.get_code("get_module_docs", {"module": package_name})
        response = await agent.context.evaluate(
            code,
            parent_header={},
        )
        return response["return"]


    @tool()
    async def get_function_docstring(self, function_name: str, agent: AgentRef):
        """
        Use this tool to additional information on individual function such as their inputs, outputs and descrption (and generally anything else that would be in a docstring)

        Read the information returned to learn how to use the function and which arguments they take.

        The function names used in the input to this tool should include the entire module hierarchy

        If this fails, this means the function does not exist.

        Args:
            function_name (str): name of the function to lookup.
        """
        code = f"""
            import DisplayAs, JSON3
            try {function_name}
            catch
                DisplayAs.unlimited(
                    JSON3.write(
                        Dict("docs" => "{function_name} not defined")
                    )
                )
            else
                docstring = string(@doc({function_name}))
                doc_object = Dict("docs" => docstring)
                DisplayAs.unlimited(
                    JSON3.write(doc_object)
                )
            end
        """
        response = await agent.context.beaker_kernel.evaluate(
            code,
            parent_header={},
        )
        docs = response["return"]["docs"]
        return docs
