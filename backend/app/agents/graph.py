from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.nodes import chat_node, tool_node
from langgraph.prebuilt import tools_condition

workflow = StateGraph(AgentState)

workflow.add_node("agent", chat_node)
workflow.add_node("tools", tool_node)

workflow.set_entry_point("agent")
workflow.add_conditional_edges("agent", tools_condition, {"tools": "tools", "__end__": END})
workflow.add_edge("tools", "agent")

app_graph = workflow.compile()
