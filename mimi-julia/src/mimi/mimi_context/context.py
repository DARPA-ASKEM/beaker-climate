# SPDX-FileCopyrightText: 2024-present Brandon Rose <rose.brandon.m@gmail.com>
#
# SPDX-License-Identifier: MIT
from typing import Dict, Any, TYPE_CHECKING

from beaker_kernel.lib import BeakerContext
from beaker_kernel.lib.utils import action

from .agent import MimiAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel


class MimiContext(BeakerContext):
    """
    Mimi.jl context for Beaker.
    """

    compatible_subkernels = ["julia"]
    SLUG = "mimi"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]):
        self.library_name="Mimi.jl"
        self.imported_modules={}
        self.available_modules={}
        self.sub_module_description=[]
        self.variables={}
        self.few_shot_examples=''        
        super().__init__(beaker_kernel, MimiAgent, config)

    async def setup(self, context_info=None, parent_header=None):
        # Custom setup can be done here
        pass

    async def auto_context(self):
        from .lib.dynamic_example_selector import query_examples
        # await self.get_jupyter_context()
        most_recent_user_query=''
        for message in self.agent.messages:
            if message['role']=='user':
                most_recent_user_query=message['content']
            self.few_shot_examples=query_examples(most_recent_user_query)
            self.agent.debug(event_type="few_shot_examples",content={
                        "few_shot_examples": self.few_shot_examples,
                        "user_query":most_recent_user_query
                    })

        
        intro_manual3_few_no_repl_all_classes=f"""You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.
{self.library_name} is a framework for representing systems using ontology-grounded meta-model templates, and generating various model implementations and exchange formats from these templates. 
It also implements algorithms for assembling and querying domain knowledge graphs in support of modeling.

You should ALWAYS try looking up the what the user is asking you to do or portions of what the user is asking you to do in the documentation to get a sense of how it can be done.
You should ALWAYS think about which functions and classes from {self.library_name} you are going to use before you write code. Try to use {self.library_name} as much as possible.
You can do so in the following ways: 
If the functions you want to use are in the context below, no need to look them up again.
Otherwise, first try to use the Toolset.search_functions_classes to search for relevant functions and classes.
If that does not provide enough information, lookup the available functions for related modules using Toolset.get_available_functions.
If there is a main class or function you are using, you can lookup all the information on it and all the objects and functions required to use it using Toolset.get_class_or_function_full_information.
Use this when you want to instantiate a complicated object.

You can lookup source code for individual functions or classes using the Toolset.get_functions_and_classes_source_code before using a function from {self.library_name}.

Below is some information on the submodules in {self.library_name}:

{self.sub_module_description}
        
Additionally here are some similar examples of similar user requests and your previous successful code generations in the format [[Request,Code]].
If the request from the user is similar enough to one of these examples, use it to help write code to answer the user's request.
    
{self.few_shot_examples}
"""

        '''If there is a main class or function you are using, you can lookup all the information on it and all the objects and functions required to use it using Toolset.get_class_or_function_full_information.
        Use this when you want to instantiate a complicated object.'''


        code_environment2=f"""These are the variables in the user's current code environment with key value pairs:
{self.variables}

The user has also imported the following modules: {self.imported_modules}.
The following modules are installed and available to be imported: {self.available_modules}.
So you don't need to import them when generating code.
When writing code that edits the variables that the user has in their environment be sure to modify them in place. 
For example if we have a variable a=1, if we wanted to change a to 2, we you write a=2.
When the user asks you to perform an action, if they specifically mention a variable name, be sure to use that variable.
Additionally if the object they ask you to update is similar to an object in the code environment, be sure to use that variable. 
"""

        outro = f"""
Please answer any user queries or perform user instructions to the best of your ability, but do not guess if you are not sure of an answer.
"""
        result = "\n".join([intro_manual3_few_no_repl_all_classes,code_environment2,outro])
        return result