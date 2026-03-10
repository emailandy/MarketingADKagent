import os
import sys

# Fix sys.path to include ADK source
# Assuming this script is run from the root of marketing-agency/
adk_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ADK/src'))
sys.path.insert(0, adk_src)

from google.adk.apps import App
from .agents.marketing_manager import marketing_manager

# Create the Marketing Agency App
marketing_app = App(
    name="MarketingDepartment",
    root_agent=marketing_manager
)

if __name__ == "__main__":
    print("Marketing Agency App initialized successfully.")
