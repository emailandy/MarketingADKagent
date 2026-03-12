from google.adk import Agent
from google.adk.tools.google_search_tool import google_search
from google.adk.tools.google_maps_grounding_tool import google_maps_grounding
from google.genai import types

# Common config for Gemini 3 Flash (Optimized for Speed)
gemini_3_flash_config = types.GenerateContentConfig()

# App Store Optimizer
app_store_optimizer = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='app_store_optimizer',
    output_key='aso_strategy_report',
    description='Expert app store marketing specialist focused on ASO and conversion.',
    instruction="""
    You are App Store Optimizer. Your mission is to maximize organic downloads and improve app rankings.
    Ground your strategy in real-time market trends using Google Search and local app availability via Google Maps.
    Focus on keyword research, metadata optimization (titles, descriptions), and visual asset strategy.
    Always be data-driven and conversion-focused.
    """,
    tools=[google_search, google_maps_grounding]
)

# Growth Hacker
growth_hacker = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='growth_hacker',
    output_key='growth_hacking_plan',
    description='Expert growth strategist specializing in rapid user acquisition.',
    instruction="""
    You are Growth Hacker. Your mission is rapid user acquisition through experimentation.
    Use Google Search to find emerging growth channels and Google Maps to identify local acquisition opportunities.
    Develop viral loops, optimize conversion funnels, and find scalable growth channels.
    Focus on K-factor, CAC, and LTV.
    """,
    tools=[google_search, google_maps_grounding]
)

# Social Media Strategist
social_media_strategist = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='social_media_strategist',
    output_key='social_media_roadmap',
    description='Expert social media strategist for professional platforms.',
    instruction="""
    You are Social Media Strategist. Your mission is to build brand authority across platforms like LinkedIn and Twitter.
    Use Google Search for trending topics and Google Maps for local community event research.
    Create cross-platform campaigns, build communities, and manage real-time engagement.
    Focus on thought leadership and integrated campaign management.
    """,
    tools=[google_search, google_maps_grounding]
)

# Content Creator
content_creator = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='content_creator',
    output_key='content_strategy_brief',
    description='Expert content strategist and storyteller.',
    instruction="""
    You are Content Creator. Your mission is to develop compelling multi-platform content.
    Ground your storytelling in facts from Google Search and local context from Google Maps.
    Focus on editorial calendars, brand storytelling, and audience engagement across all digital channels.
    """,
    tools=[google_search, google_maps_grounding]
)

# SEO Specialist
seo_specialist = Agent(
    model='gemini-3-flash-preview',
    generate_content_config=gemini_3_flash_config,
    name='seo_specialist',
    output_key='seo_audit_and_plan',
    description='Expert search engine optimization strategist.',
    instruction="""
    You are SEO Specialist. Your mission is to drive sustainable organic search growth.
    Use Google Search for real-time SERP analysis and Google Maps for local SEO audits.
    Focus on technical SEO, content optimization, link authority building, and topical authority.
    Always follow white-hat techniques and focus on user intent.
    """,
    tools=[google_search, google_maps_grounding]
)
