import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set project and location for Vertex AI
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"
os.environ["GOOGLE_CLOUD_PROJECT"] = "nodepeel"
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"

import asyncio
from backend.agents.titan_analyst import titan_analyst
from google.adk.runners import InMemoryRunner
from google.genai import types

async def run_titan_query(runner, user_message: str) -> str:
    content = types.Content(
        role='user',
        parts=[types.Part.from_text(text=user_message)]
    )
    
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
    return response_text

async def test_titan_agent():
    print("Testing Titan Analyst Agent locally...")
    
    runner = InMemoryRunner(agent=titan_analyst)
    runner.auto_create_session = True
    
    # Test case 1: Analyze China market share
    query = "Analyze the China market for 2025. How did Agoda perform compared to the official government arrivals?"
    print(f"\nQuery: {query}")
    response = await run_titan_query(runner, query)
    print(f"Response:\n{response}")
    
    # Test case 2: Executive briefing Q&A
    query = "Thailand just crossed 30 million arrivals. How does Agoda's growth compare to the overall market recovery?"
    print(f"\nQuery: {query}")
    response = await run_titan_query(runner, query)
    print(f"Response:\n{response}")

if __name__ == "__main__":
    asyncio.run(test_titan_agent())
