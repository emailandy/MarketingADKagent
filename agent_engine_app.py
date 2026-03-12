import os
import sys
import logging

# Configure logging to stdout so it shows up in cloud logs
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

# CRITICAL: Set location to global BEFORE any imports
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "nodepeel"

try:
    logger.info("Importing marketing_manager...")
    from backend.agents.marketing_manager import marketing_manager
    logger.info("Import successful.")
    
    # Entry point for ADK deployment to Agent Engine
    root_agent = marketing_manager
    logger.info("root_agent assigned.")
except Exception as e:
    logger.error(f"STARTUP ERROR: {str(e)}", exc_info=True)
    # Re-raise so ADK knows startup failed, but we want the logs first
    raise
