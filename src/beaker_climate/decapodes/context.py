from typing import Dict, Any, TYPE_CHECKING

from beaker_kernel.lib import BeakerContext
from beaker_kernel.lib.subkernels.julia import JuliaSubkernel
from beaker_kernel.lib.utils import action

from .agent import DecapodesAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import BeakerKernel
    from beaker_kernel.lib.agent import BeakerAgent


class DecapodesContext(BeakerContext):
    """
    This is the context class.
    """

    compatible_subkernels = ["julia"]
    SLUG = "decapodes"
    agent_cls: "BeakerAgent"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]):
        super().__init__(beaker_kernel, DecapodesAgent, config)
        if not isinstance(self.subkernel, JuliaSubkernel):
            raise ValueError("This context is only valid for Julia.")

    async def setup(self, context_info=None, parent_header=None):
        await super().setup(context_info=context_info, parent_header=parent_header)
