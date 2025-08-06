# 🧠 Thread-Aware Conversational AI Chatbot using LangGraph and Gemini

A context-aware chatbot built using **LangGraph** and **Gemini 2.0 Flash** that maintains conversation memory based on a unique `thread_id`, enabling personalized, multi-turn interactions. Integrated with a **Streamlit** frontend for real-time chat visualization.

---

## 🚀 Features

- 💬 **Multi-turn conversations** with session-level memory
- 🧠 **Thread-specific context** retention using `thread_id`
- ⚙️ **LangGraph-powered agent workflow** with state management
- 🌐 **Gemini 2.0 Flash** used as the LLM backbone
- 📊 **Streamlit UI** for interactive chat simulation
- 💾 In-memory checkpointing via `InMemorySaver` for simplicity

---

## 📁 Project Structure

chatbot/
│
├── chatbot.py # LangGraph backend workflow
├── app.py # Streamlit frontend
├── .env # API keys and environment variables
├── requirements.txt # Python dependencies
└── README.md # Project documentation
