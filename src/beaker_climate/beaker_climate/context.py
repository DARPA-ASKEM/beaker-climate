import logging
import os
from typing import TYPE_CHECKING, Any, Dict

from archytas.tool_utils import LoopControllerRef

from beaker_kernel.lib import BeakerContext
from beaker_kernel.lib.utils import intercept

from .agent import ClimateDataUtilityAgent
import pathlib

if TYPE_CHECKING:
    from beaker_kernel.lib import BeakerContext

logger = logging.getLogger(__name__)

class ClimateDataUtilityContext(BeakerContext):
    """
    You are an agent that loads and helps analyze climate, hydro, atmospheric, and ocean data.
    """
    compatible_subkernels = ["python3"]
    SLUG = "beaker_climate"

    def __init__(self, beaker_kernel: "BeakerKernel", config: Dict[str, Any]) -> None:
        super().__init__(beaker_kernel, ClimateDataUtilityAgent, config)

    async def setup(self, context_info=None, parent_header=None):
        # Custom setup can be done here
        pangeo_url = pathlib.Path(__file__).parent / 'catalogs/master.yaml'
        await self.evaluate(f'__pangeo_url = "{pangeo_url}"')
        noaa_url = pathlib.Path(__file__).parent / 'api_documentation/noaa_catalog.yaml'
        await self.evaluate(f'__noaa_url = "{noaa_url}"')
        code = self.get_code("setup")
        await self.evaluate(code)
