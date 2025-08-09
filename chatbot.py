from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START, add_messages
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class ChatbotSchema(TypedDict):
    
    messages: Annotated[list[BaseMessage], add_messages]

def chatnode(state: ChatbotSchema):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages":[response]}

conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)
graph = StateGraph(ChatbotSchema)

graph.add_node("chatbot", chatnode)

graph.add_edge(START,"chatbot")
graph.add_edge("chatbot",END)
checkpointer = SqliteSaver(conn=conn)
workflow = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)
# config = {"configurable":{"thread_id":"1"}}

# user_input = input("Enter you input: ")


# for msg_chunk, metadat in  workflow.stream(
#     {"messages": HumanMessage(content=user_input)},config=config,
#     stream_mode="messages"):

#     if msg_chunk.content:
#         print(msg_chunk.content, end=" ", flush=True)

# 
# while True:
#     
#     if user_input.lower().strip() in ["exit","quit"]:
#         print("Bye...")
#         break
#     else:

#         res = workflow.invoke({"messages": HumanMessage(content=user_input)},config=config)
#         print(res["messages"][-1].content)


