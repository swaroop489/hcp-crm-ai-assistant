from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import Optional

class LogInteractionInput(BaseModel):
    hcp_name: str = Field(description="Name of the Healthcare Professional")
    interaction_type: str = Field(description="Type of interaction (e.g., Meeting, Email, Call)")
    date: Optional[str] = Field(None, description="Date of interaction in YYYY-MM-DD format")
    topics_discussed: str = Field(description="Key topics discussed")
    sentiment: str = Field(description="Observed sentiment: Positive, Neutral, or Negative")
    materials_shared: Optional[str] = Field(None, description="Materials or brochures shared")

@tool("log_interaction", args_schema=LogInteractionInput)
def log_interaction_tool(hcp_name: str, interaction_type: str, topics_discussed: str, sentiment: str, date: Optional[str] = None, materials_shared: Optional[str] = None):
    """
    Logs a new interaction with a Healthcare Professional.
    """
    return f"Successfully logged interaction with {hcp_name}. Topics: {topics_discussed}. Sentiment: {sentiment}."

class EditInteractionInput(BaseModel):
    field_to_update: str = Field(description="The field to update (e.g., hcp_name, sentiment, topics_discussed)")
    new_value: str = Field(description="The new value for the field")

@tool("edit_interaction", args_schema=EditInteractionInput)
def edit_interaction_tool(field_to_update: str, new_value: str):
    """
    Edits a previously logged interaction by updating specific fields.
    """
    return f"Successfully updated {field_to_update} to {new_value}."

@tool("search_hcp")
def search_hcp_tool(query: str):
    """
    Searches for a Healthcare Professional by name or specialization.
    """
    return f"Search results for HCP matching '{query}': Found records."

@tool("recommend_follow_up")
def recommend_follow_up_tool(interaction_summary: str):
    """
    Recommends a follow-up action based on the recent interaction summary.
    """
    return f"Recommended follow up: Send a thank you email and schedule a follow-up meeting in 2 weeks."

@tool("generate_interaction_summary")
def generate_interaction_summary_tool(hcp_name: str):
    """
    Generates a brief summary of the most recent interaction with the specified HCP.
    """
    return f"Summary for {hcp_name}: Discussed product efficacy. HCP was highly receptive."

tools = [
    log_interaction_tool,
    edit_interaction_tool,
    search_hcp_tool,
    recommend_follow_up_tool,
    generate_interaction_summary_tool
]
