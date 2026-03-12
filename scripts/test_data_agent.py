import sys
import os

# Add backend/agents to sys.path
sys.path.append(os.path.join(os.getcwd(), 'backend', 'agents'))

try:
    from data_analyst import ota_data_query
except ImportError as e:
    print(f"FAILED to import data_analyst: {e}")
    sys.exit(1)

def run_test_queries():
    questions = [
        "Which regions have the lowest ROAS (Returns on Ad spend) and which channels are dragging them down?",
        "What are the top 3 most efficient marketing channels by ROAS across all regions?",
        "Show me regions where actual spend significantly exceeds planned budget but ROAS is below 3.0"
    ]
    
    print("--- DATA AGENT VERIFICATION ---")
    
    for i, q in enumerate(questions, 1):
        print(f"\nQUERY {i}: {q}")
        print("RESULT:")
        try:
            # We wrap this in a try-except because the environment might not have the 
            # google-cloud-geminidataanalytics library installed yet in THIS specific context.
            res = ota_data_query(q)
            print(res)
        except Exception as e:
            print(f"ERROR executing query: {e}")

if __name__ == "__main__":
    run_test_queries()
