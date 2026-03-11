import os
from .marketing_manager import marketing_manager

# Override location to global for Gemini 3.1 Pro Preview access
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

# Entry point for ADK deployment to Agent Engine
root_agent = marketing_manager
