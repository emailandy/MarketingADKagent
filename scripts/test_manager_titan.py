import sys
import os
import asyncio

# Fix sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(current_dir))

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "nodepeel"
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

from backend.agents.marketing_manager import marketing_manager
from google.adk.runners import InMemoryRunner
from google.genai import types

async def test_manager_titan():
    runner = InMemoryRunner(agent=marketing_manager)
    runner.auto_create_session = True
    
    content = types.Content(
        role='user',
        parts=[types.Part.from_text(text="Do you have access to a Titan Analyst? If so, what is the executive summary for Thailand 2025?")]
    )
    
    print("Querying Marketing Manager...")
    response_text = ""
    async for event in runner.run_async(
        user_id="test_user",
        session_id="test_session",
        new_message=content
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    response_text += part.text
                    print(part.text, end="", flush=True)
    print("\n--- Final Response ---")
    print(response_text)

if __name__ == "__main__":
    asyncio.run(test_manager_titan())
