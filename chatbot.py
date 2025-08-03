from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START, add_messages
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, BaseMessage

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

print(llm.invoke("hi"))

# class ChatbotSchema(TypedDict):
#     messages: Annotated[list[BaseMessage], add_messages]

# def chatnode(state: ChatbotSchema):
#     response = llm.invoke(state["messages"])
#     return {"message":[response]}

# grpah = StateGraph(ChatbotSchema)

# grpah.add_node("chatbot", chatnode)

# grpah.add_edge(START,"chatbot")
# grpah.add_edge("chatbot",END)

# workflow = grpah.compile()

# print(workflow.invoke({"message":"hi"}))