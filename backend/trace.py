import os
from dotenv import load_dotenv
load_dotenv()
from app.agents.graph import app_graph
from langchain_core.messages import HumanMessage
print('Starting graph...')
events = app_graph.stream({'messages': [HumanMessage(content='I met with Dr. Smith today. We discussed XYZ, and the sentiment was positive.')]}, stream_mode="values")
for event in events:
    msg = event['messages'][-1]
    print(f"{type(msg).__name__}: {msg.content}")
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        print(f"Tool calls: {msg.tool_calls}")
