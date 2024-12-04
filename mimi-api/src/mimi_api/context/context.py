from typing import TYPE_CHECKING, Any, Dict, List

from beaker_kernel.lib.context import BaseContext
from beaker_kernel.lib.subkernels.julia import JuliaSubkernel

from .agent import MimiApiAgent

if TYPE_CHECKING:
    from beaker_kernel.kernel import LLMKernel
    from beaker_kernel.lib.agent import BaseAgent

class MimiApiContext(BaseContext):
    compatible_subkernels = ["julia"]
    SLUG = "mimi_api"
    agent_cls: "BaseAgent" = MimiApiAgent

    def __init__(self, beaker_kernel: "LLMKernel", config: Dict[str, Any]):
        super().__init__(beaker_kernel, self.agent_cls, config)
        if not isinstance(self.subkernel, JuliaSubkernel):
            raise ValueError("This context is only valid for Julia.")
