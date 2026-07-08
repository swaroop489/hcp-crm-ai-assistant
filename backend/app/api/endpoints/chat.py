from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.graph import app_graph
from langchain_core.messages import HumanMessage

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    try:
        initial_state = {"messages": [HumanMessage(content=request.message)]}
        
        # Execute the LangGraph workflow
        final_state = app_graph.invoke(initial_state)
        
        # Extract the last message from the agent
        ai_message = final_state["messages"][-1].content
        
        # Extract state to pass back to frontend (can be used to update Redux store)
        state_dump = {"messages": [m.dict() for m in final_state["messages"]]}
        
        return ChatResponse(
            response=ai_message,
            updated_state=state_dump
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
