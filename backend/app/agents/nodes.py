from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage
from app.agents.tools import tools
from app.agents.prompts import SYSTEM_PROMPT
from app.services.groq_service import get_llm

llm = get_llm()
llm_with_tools = llm.bind_tools(tools)

def chat_node(state):
    messages = state["messages"]
    
    # Prepend the system prompt if not present
    if not any(isinstance(m, SystemMessage) for m in messages):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
        
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)
