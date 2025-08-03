from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START, add_messages
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

