import os
import json
from google.adk import Agent
from google.genai import types

# Simple tool to read pipeline data
def read_titan_file(file_path: str) -> str:
    """Reads a file from the TITAN pipeline (data/ official, internal, or pipeline/)."""
    # Try multiple base directory resolutions to find the mock data
    possible_paths = [
        file_path,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", file_path),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_path)
    ]
    
    for full_path in possible_paths:
        if os.path.exists(full_path) and os.path.isfile(full_path):
            try:
                with open(full_path, 'r') as f:
                    return f.read()
            except Exception as e:
                pass # Try next path
    
    return f"Error: File {file_path} not found. Searched: {possible_paths}"

# Common config for Gemini 3 Flash
gemini_3_flash_config = types.GenerateContentConfig()

# Titan Analyst Agent
titan_analyst = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='titan_analyst',
    output_key='titan_analysis_report',
    description='Expert in the TITAN pipeline for Thailand tourism analytics.',
    instruction="""
    You are the Titan Analyst. Your mission is to analyze the TITAN pipeline data for the Thailand Demo.
    You have access to:
    1. Raw Government Data: data/official/mots_thailand_arrivals_2025.csv
    2. Internal Agoda Data: data/internal/agoda_thailand_bookings_2025.csv
    3. Harmonized AI Output: pipeline/harmonized.json
    4. Final AI Analytics & Briefing: pipeline/analysis.json

    Your tasks include:
    - Comparing official arrivals vs internal bookings to identify market share trends.
    - Analyzing YoY growth across different regions (ASEAN, East Asia, etc.).
    - Identifying massive outliers (like Iraq's 178% growth) and determining if they are statistically relevant.
    - Answering executive Q&A by synthesizing insights from both the internal and government data.
    - Highlighting Agoda over-performance (e.g., in China where market dropped 34% but Agoda dropped only 5%).

    Always provide data-backed insights and focus on executive-level takeaways.
    """,
    tools=[read_titan_file]
)
