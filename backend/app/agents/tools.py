from langchain_core.tools import tool
from pydantic import BaseModel, Field
from typing import Optional
from app.database.database import SessionLocal
from app.database.models import HCP, Interaction, SentimentEnum
from datetime import datetime

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
    """
    Logs a new interaction with a Healthcare Professional in the MySQL database.
    """
    db = SessionLocal()
    try:
        # Map sentiment string to Enum
        sentiment_val = SentimentEnum.NEUTRAL
        if sentiment.lower() == "positive":
            sentiment_val = SentimentEnum.POSITIVE
        elif sentiment.lower() == "negative":
            sentiment_val = SentimentEnum.NEGATIVE

        # Parse date and time if available
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date() if date else datetime.now().date()
        parsed_time = datetime.strptime(time, "%H:%M").time() if time else datetime.now().time()

        new_interaction = Interaction(
            hcp_id=hcp_id,
            interaction_type=interaction_type,
            date=parsed_date,
            time=parsed_time,
            topics_discussed=topics_discussed,
            materials_shared=materials_shared,
            sentiment=sentiment_val,
            outcomes=outcomes,
            follow_up_actions=follow_up_actions
        )
        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)
        return f"Successfully logged interaction ID {new_interaction.id} for HCP ID {hcp_id}. Topics: {topics_discussed}."
    except Exception as e:
        db.rollback()
        return f"Error logging interaction: {str(e)}"
    finally:
        db.close()


class EditInteractionInput(BaseModel):
    interaction_id: int = Field(description="The ID of the interaction to update")
    field_to_update: str = Field(description="The field to update (e.g., sentiment, topics_discussed, outcomes)")
    new_value: str = Field(description="The new value for the field")

@tool("edit_interaction", args_schema=EditInteractionInput)
def edit_interaction_tool(interaction_id: int, field_to_update: str, new_value: str):
    """
    Edits a previously logged interaction by updating specific fields in the MySQL database.
    """
    db = SessionLocal()
    try:
        interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
        if not interaction:
            return f"Interaction with ID {interaction_id} not found."
        
        # Handle sentiment enum special case
        if field_to_update == "sentiment":
            if new_value.lower() == "positive":
                new_value = SentimentEnum.POSITIVE
            elif new_value.lower() == "negative":
                new_value = SentimentEnum.NEGATIVE
            else:
                new_value = SentimentEnum.NEUTRAL
        
        if hasattr(interaction, field_to_update):
            setattr(interaction, field_to_update, new_value)
            db.commit()
            return f"Successfully updated {field_to_update} to {new_value} for interaction {interaction_id}."
        else:
            return f"Field {field_to_update} does not exist on Interaction model."
    except Exception as e:
        db.rollback()
        return f"Error updating interaction: {str(e)}"
    finally:
        db.close()


class SearchHCPInput(BaseModel):
    query: str = Field(description="Name or specialization of the HCP to search for")

@tool("search_hcp", args_schema=SearchHCPInput)
def search_hcp_tool(query: str):
    """
    Searches for a Healthcare Professional in the database by name.
    """
    db = SessionLocal()
    try:
        hcps = db.query(HCP).filter(HCP.name.ilike(f"%{query}%")).all()
        if not hcps:
            return f"No HCP found matching '{query}'."
        
        results = [f"ID: {h.id}, Name: {h.name}, Specialization: {h.specialization}" for h in hcps]
        return "Found HCPs:\n" + "\n".join(results)
    finally:
        db.close()


class RecommendFollowUpInput(BaseModel):
    interaction_summary: str = Field(description="Summary of the interaction")

@tool("recommend_follow_up", args_schema=RecommendFollowUpInput)
def recommend_follow_up_tool(interaction_summary: str):
    """
    Generates a follow-up recommendation based on the interaction.
    """
    if "positive" in interaction_summary.lower():
        return "Recommended: Schedule a follow-up meeting in 2 weeks to discuss next steps and share a product sample."
    elif "negative" in interaction_summary.lower():
        return "Recommended: Send a polite follow-up email addressing concerns and providing additional clinical data."
    else:
        return "Recommended: Send standard thank you email."


class GenerateInteractionSummaryInput(BaseModel):
    interaction_id: int = Field(description="The ID of the interaction to summarize")

@tool("generate_interaction_summary", args_schema=GenerateInteractionSummaryInput)
def generate_interaction_summary_tool(interaction_id: int):
    """
    Generates a summary of an existing interaction from the database.
    """
    db = SessionLocal()
    try:
        interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()
        if not interaction:
            return f"Interaction {interaction_id} not found."
        
        sentiment_val = interaction.sentiment.value if interaction.sentiment else 'Unknown'
        return f"Interaction ID {interaction_id} summary: Discussed {interaction.topics_discussed}. Sentiment was {sentiment_val}."
    finally:
        db.close()

tools = [
    log_interaction_tool,
    edit_interaction_tool,
    search_hcp_tool,
    recommend_follow_up_tool,
    generate_interaction_summary_tool
]
