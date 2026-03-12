import os
import sys

# CRITICAL: Set location to global BEFORE any imports
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from .marketing_manager import marketing_manager

# Entry point for ADK deployment to Agent Engine
root_agent = marketing_manager
