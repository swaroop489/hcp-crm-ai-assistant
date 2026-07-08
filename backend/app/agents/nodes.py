from langgraph.prebuilt import ToolNode
from app.agents.tools import tools
from app.services.groq_service import get_llm

llm = get_llm()
llm_with_tools = llm.bind_tools(tools)

def chat_node(state):
    messages = state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

tool_node = ToolNode(tools)
