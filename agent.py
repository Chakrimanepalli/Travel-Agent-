from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient
import os

# Initialize MCP Toolbox client
toolbox_url = os.getenv('MCP_TOOLBOX_URL', 'http://localhost:5000')
toolbox = ToolboxSyncClient(toolbox_url)

# Load all tools from the travel_toolset
tools = toolbox.load_toolset('travel_toolset')

# Create the Travel Agent
travel_agent = Agent(
    name="travel_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "An intelligent travel assistant that helps users find and book hotels. "
        "Provides information about hotels by location, name, and availability."
    ),
    instruction=(
        "You are a friendly and helpful travel assistant. "
        "Help users find hotels based on their preferences including location, budget, and dates. "
        "Use the available tools to search the hotel database and provide accurate information. "
        "When presenting hotel options, format them clearly with name, location, and price tier. "
        "Always be courteous and ask clarifying questions when needed. "
        "If a user asks about something outside of hotel bookings, politely redirect them."
    ),
    tools=tools,
)
