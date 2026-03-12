import os
from google.adk import Agent
from google.genai import types
from google.cloud import geminidataanalytics

# Configuration for BigQuery OTA Data
PROJECT_ID = "nodepeel"
DATASET_ID = "marketing_analytics"
TABLE_ID = "ota_performance_weekly"
LOCATION = "global"

def ota_data_query(query: str) -> str:
    """
    Query the OTA Marketing performance dataset in BigQuery for insights.
    Use this tool to answer questions about ROAS, budget variance, channel efficiency,
    and regional performance metrics.
    
    Args:
        query: The natural language question to ask the data.
    """
    # Initialize client
    data_chat_client = geminidataanalytics.DataChatServiceClient()
    
    # Define the BigQuery Data Sources
    datasource_references = geminidataanalytics.DatasourceReferences()
    
    # Tables to include
    table_ids = [
        "ota_performance_weekly",
        "mots_arrivals_monthly",
        "market_performance_insights"
    ]
    
    for table_id in table_ids:
        bq_table = geminidataanalytics.BigQueryTableReference()
        bq_table.project_id = PROJECT_ID
        bq_table.dataset_id = DATASET_ID
        bq_table.table_id = table_id
        datasource_references.bq.table_references.append(bq_table)
    
    # Define system instructions for the agent's persona
    inline_context = geminidataanalytics.Context()
    inline_context.system_instruction = (
        "You are an expert Marketing Data Analyst specializing in OTA performance and market penetration. "
        "Analyze the data provided to identify underperforming regions, top-performing channels, "
        "and market penetration opportunities. Use the 'market_performance_insights' view to compare "
        "internal bookings against MOTS arrivals to calculate true market share and penetration velocity."
    )
    inline_context.datasource_references = datasource_references
    
    # Create the user message
    messages = [geminidataanalytics.Message()]
    messages[0].user_message.text = query
    
    # Send the request
    # Note: Using the provided parent format
    parent = f"projects/{PROJECT_ID}/locations/{LOCATION}"
    request = geminidataanalytics.ChatRequest(
        parent=parent,
        inline_context=inline_context,
        messages=messages,
    )
    
    # Handle the streaming response and aggregate
    full_response = ""
    parts_received = 0
    try:
        stream = data_chat_client.chat(request=request)
        for response in stream:
            if hasattr(response, 'system_message'):
                # Extract text parts from the response
                if hasattr(response.system_message, 'text'):
                    for part in response.system_message.text.parts:
                        parts_received += 1
                        if isinstance(part, str):
                            full_response += part
                        elif hasattr(part, 'text'):
                            full_response += part.text
                        else:
                            # Fallback or debug for truly unknown parts
                            full_response += f"\n[Unknown part type: {type(part)}]\n"
        
        if not full_response:
            return f"No insights generated. Received {parts_received} parts."
        return full_response
        
    except Exception as e:
        return f"Error querying OTA data: {str(e)}"

# Data Analyst Agent
data_analyst = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=types.GenerateContentConfig(),
    name='data_analyst',
    output_key='ota_data_insights',
    description='Expert Marketing Data Analyst for OTA BigQuery datasets.',
    instruction="""
    You are the Data Analyst. Your mission is to provide deep, data-driven insights from the BigQuery OTA dataset.
    Use the `ota_data_query` tool to answer Michael Torres' questions about:
    - ROAS (Return on Ad Spend) and regional performance.
    - Market Penetration (Bookings vs MOTS Arrivals) and True Market Share.
    - Growth Velocity: Comparing MOTS growth vs Internal Booking growth.
    - Budget variance and efficiency (CAC) relative to market opportunity.
    
    When an orchestrator or user asks a data-related question, always use the tool to get the most accurate answer.
    Synthesize the raw data insights into a clear narrative with priority recommendations.
    """,
    tools=[ota_data_query]
)
