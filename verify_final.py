
import os
import vertexai
from vertexai.preview.reasoning_engines import ReasoningEngine

# Configuration
PROJECT_ID = "nodepeel"
LOCATION = "us-central1"
REASONING_ENGINE_ID = "1292690323218104320"

vertexai.init(project=PROJECT_ID, location=LOCATION)

def test_agent():
    print(f"Testing Agent Engine: {REASONING_ENGINE_ID}...")
    try:
        remote_agent = ReasoningEngine(f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{REASONING_ENGINE_ID}")
        
        # Test Query
        print("\nSending query 'Hello'...")
        # Omitting session_id to let the agent auto-generate it
        response = remote_agent.query(
            message="Hello",
            user_id="defaultuser"
        )
        print(f"Response: {response}")
        
        if response:
            print("\nSUCCESS: Received a response!")
        else:
            print("\nFAILURE: Received a blank response.")
            
    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_agent()
