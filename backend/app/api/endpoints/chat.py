from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.agents.graph import app_graph
from langchain_core.messages import HumanMessage, AIMessage

router = APIRouter()

@router.post("/", response_model=ChatResponse)
def chat_with_agent(request: ChatRequest):
    try:
        # Inject the currently selected HCP ID from the UI to help the AI
        context = f"System Context: The user has currently selected HCP ID {request.hcp_id} in the UI.\n\n" if request.hcp_id else ""
        full_message = context + request.message
        
        initial_state = {"messages": [HumanMessage(content=full_message)]}
        final_state = app_graph.invoke(initial_state)
        
        ai_message = final_state["messages"][-1].content
        
        # Extract tool arguments to auto-fill the UI
        form_data = {}
        for m in reversed(final_state["messages"]):
            if isinstance(m, AIMessage) and getattr(m, 'tool_calls', None):
                for tc in m.tool_calls:
                    if tc["name"] in ["log_interaction", "edit_interaction"]:
                        form_data.update(tc["args"])
                if form_data:
                    break  # Found the relevant tool call, can stop searching
                
        state_dump = {"form_data": form_data}
        
        return ChatResponse(
            response=ai_message or "Done.",
            updated_state=state_dump
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
