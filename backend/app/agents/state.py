from typing import TypedDict, List, Annotated
from langgraph.graph.message import AnyMessage, add_messages

class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
