from google.adk import Agent
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.google_maps_grounding_tool import google_maps_grounding
from google.genai import types
from .specialists import (
    app_store_optimizer,
    growth_hacker,
    social_media_strategist,
    content_creator,
    seo_specialist
)
from .data_analyst import data_analyst
from .titan_analyst import titan_analyst

# Marketing Manager (Orchestrator)
marketing_manager = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=types.GenerateContentConfig(),
    name='marketing_manager',
    description='Professional Marketing Department Orchestrator.',
    instruction="""
    You are the Marketing Manager. Your goal is to lead the Marketing Department and coordinate specialized agents to achieve business goals.
    Use Google Search and Google Maps to ground your recommendations in real-time data and local context.
    
    Your specialized team:
    1. App Store Optimizer: For mobile app discoverability and conversion.
    2. Growth Hacker: For rapid acquisition and viral loops.
    3. Social Media Strategist: For brand authority and community building.
    4. Content Creator: For storytelling and multi-platform content.
    5. SEO Specialist: For sustainable organic search growth.
    6. Data Analyst: For deep insights from our BigQuery OTA performance datasets (ROAS, budget variance, etc.).
    7. Titan Analyst: For analysis of the TITAN pipeline (Thailand Demo) including government tourism data, internal Agoda bookings, and harmonized growth metrics.
    
    When you receive a request:
    - Analyze the goal and identify which specialist(s) are needed.
    - Delegate parts of the task to the relevant specialists.
    - Synthesize their work into a cohesive marketing strategy or execution plan.
    - Communicate strategically and focus on results.
    """,
    sub_agents=[
        app_store_optimizer,
        growth_hacker,
        social_media_strategist,
        content_creator,
        seo_specialist,
        data_analyst,
        titan_analyst
    ],
    tools=[google_search, google_maps_grounding]
)
