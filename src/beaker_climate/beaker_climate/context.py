import logging
import os
from typing import TYPE_CHECKING, Any, Dict

from archytas.tool_utils import LoopControllerRef

from beaker_kernel.lib import BeakerContext
from beaker_kernel.lib.utils import intercept

from .agent import ClimateDataUtilityAgent

if TYPE_CHECKING:
    from beaker_kernel.lib import BeakerContext

logger = logging.getLogger(__name__)

class ClimateDataUtilityContext(BeakerContext):
    compatible_subkernels = ["python3"]
    SLUG = "beaker_climate"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]) -> None:
        super().__init__(beaker_kernel, ClimateDataUtilityAgent, config)

    async def setup(self, context_info=None, parent_header=None):
        # Custom setup can be done here
        code = self.get_code("setup")
        await self.evaluate(code)