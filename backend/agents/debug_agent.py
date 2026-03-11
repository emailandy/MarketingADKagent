from google.adk import Agent
import os

# Minimal agent for debugging
root_agent = Agent(
    model='gemini-1.5-flash', # Use a stable model
    name='debug_agent',
    description='Minimal debug agent.',
    instruction="Respond with 'Hello from debug agent'."
)
