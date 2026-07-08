from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import Optional
from app.database.database import SessionLocal
from app.database import crud
from app.services import parser, summarizer

class LogInteractionInput(BaseModel):
    hcp_id: int = Field(description="ID of the Healthcare Professional")
    interaction_type: str = Field(description="Type of interaction (e.g., Meeting, Email, Call)")
    date: Optional[str] = Field(None, description="Date of interaction in YYYY-MM-DD format")
    time: Optional[str] = Field(None, description="Time of interaction in HH:MM format")
    topics_discussed: str = Field(description="Key topics discussed")
    sentiment: str = Field(description="Observed sentiment: Positive, Neutral, or Negative")
    materials_shared: Optional[str] = Field(None, description="Materials or brochures shared")
    outcomes: Optional[str] = Field(None, description="Key outcomes or agreements")
    follow_up_actions: Optional[str] = Field(None, description="Follow-up actions")

@tool("log_interaction", args_schema=LogInteractionInput)
def log_interaction_tool(
    hcp_id: int, 
    interaction_type: str, 
    topics_discussed: str, 
    sentiment: str, 
    date: Optional[str] = None, 
    time: Optional[str] = None,
    materials_shared: Optional[str] = None,
    outcomes: Optional[str] = None,
    follow_up_actions: Optional[str] = None
):
    """Logs a new interaction with a Healthcare Professional in the database."""
    db = SessionLocal()
    try:
        interaction_data = {
            "hcp_id": hcp_id,
            "interaction_type": interaction_type,
            "date": parser.parse_date(date),
            "time": parser.parse_time(time),
            "topics_discussed": topics_discussed,
            "materials_shared": materials_shared,
            "sentiment": parser.parse_sentiment(sentiment),
            "outcomes": outcomes,
            "follow_up_actions": follow_up_actions
        }
        new_int = crud.create_interaction(db, interaction_data)
        return f"Successfully logged interaction ID {new_int.id} for HCP ID {hcp_id}."
    except Exception as e:
        return f"Error logging interaction: {str(e)}"
    finally:
        db.close()

class EditInteractionInput(BaseModel):
    interaction_id: int = Field(description="The ID of the interaction to update")
    field_to_update: str = Field(description="The field to update (e.g., sentiment, topics_discussed)")
    new_value: str = Field(description="The new value for the field")

@tool("edit_interaction", args_schema=EditInteractionInput)
def edit_interaction_tool(interaction_id: int, field_to_update: str, new_value: str):
    """Edits a previously logged interaction by updating specific fields."""
    db = SessionLocal()
    try:
        val = parser.parse_sentiment(new_value) if field_to_update == "sentiment" else new_value
        updated = crud.update_interaction(db, interaction_id, {field_to_update: val})
        if updated:
            return f"Successfully updated {field_to_update} to {new_value} for interaction {interaction_id}."
        return f"Interaction with ID {interaction_id} not found."
    except Exception as e:
        return f"Error updating interaction: {str(e)}"
    finally:
        db.close()

class SearchHCPInput(BaseModel):
    query: str = Field(description="Name or specialization of the HCP to search for")

@tool("search_hcp", args_schema=SearchHCPInput)
def search_hcp_tool(query: str):
    """Searches for a Healthcare Professional in the database by name."""
    db = SessionLocal()
    try:
        hcps = crud.search_hcp_by_name(db, query)
        if not hcps:
            return f"No HCP found matching '{query}'."
        return "Found HCPs:\n" + "\n".join([f"ID: {h.id}, Name: {h.name}" for h in hcps])
    finally:
        db.close()

class RecommendFollowUpInput(BaseModel):
    interaction_summary: str = Field(description="Summary of the interaction")

@tool("recommend_follow_up", args_schema=RecommendFollowUpInput)
def recommend_follow_up_tool(interaction_summary: str):
    """Generates a follow-up recommendation based on the interaction."""
    if "positive" in interaction_summary.lower():
        return "Recommended: Schedule a follow-up meeting in 2 weeks."
    elif "negative" in interaction_summary.lower():
        return "Recommended: Send a polite follow-up email addressing concerns."
    return "Recommended: Send standard thank you email."

class GenerateInteractionSummaryInput(BaseModel):
    interaction_id: int = Field(description="The ID of the interaction to summarize")

@tool("generate_interaction_summary", args_schema=GenerateInteractionSummaryInput)
def generate_interaction_summary_tool(interaction_id: int):
    """Generates a summary of an existing interaction from the database."""
    db = SessionLocal()
    try:
        interaction = crud.get_interaction(db, interaction_id)
        if not interaction:
            return f"Interaction {interaction_id} not found."
        return summarizer.generate_basic_summary(interaction.topics_discussed, getattr(interaction.sentiment, 'value', 'Unknown'))
    finally:
        db.close()

tools = [
    log_interaction_tool,
    edit_interaction_tool,
    search_hcp_tool,
    recommend_follow_up_tool,
    generate_interaction_summary_tool
]
