# 🧠 Thread-Aware Conversational AI Chatbot using LangGraph and Gemini

A context-aware chatbot built using **LangGraph** and **Gemini 2.0 Flash** that maintains conversation memory based on a unique `thread_id`, enabling personalized, multi-turn interactions. Integrated with a **Streamlit** frontend for real-time chat visualization.

---

## 🚀 Features

- 💬 **Multi-turn conversations** with session-level memory
- 

- 🧠 **Thread-specific context** retention using `thread_id`
- ⚙️ **LangGraph-powered agent workflow** with state management
- 🌐 **Gemini 2.0 Flash** used as the LLM backbone
- 📊 **Streamlit UI** for interactive chat simulation
- 💾 In-memory checkpointing via `InMemorySaver` for simplicity

---
## 📁 Project Structure

```
chatbot/
│
├── chatbot.py # LangGraph backend workflow
├── app.py # Streamlit frontend
├── .env # API keys and environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```


---

## 🛠️ Tech Stack

- **LangGraph** – agent workflow and state management
- **Google Generative AI (Gemini 2.0 Flash)** – LLM responses
- **Streamlit** – web UI for real-time interaction
- **LangChain Core** – messaging formats (`HumanMessage`, etc.)
- **Python** – orchestration and backend logic

---

## 🧪 How It Works

1. User inputs are captured via Streamlit’s chat interface.
2. Each conversation is tagged with a `thread_id` (e.g., `thread-1`).
3. Messages are passed to LangGraph’s compiled workflow.
4. LangGraph handles agent logic and invokes Gemini 2.0 Flash.
5. Gemini generates a response, and memory is updated using `InMemorySaver`.
6. Streamlit displays both user and AI messages in the chat interface.

---

## 📷 Screenshots

>
<img width="1766" height="955" alt="image" src="https://github.com/user-attachments/assets/a1ecff83-b86c-4464-9ed1-ba053dda1bbb" />

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/bantee-sharma/chatbot-in-langgraph.git
cd chatbot-in-langgraph
```

