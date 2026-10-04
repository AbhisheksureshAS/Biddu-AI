# 🤖 Biddu AI

**Biddu AI** is a conversational AI chatbot built with **Streamlit, LangGraph, LangChain, and Groq**. It supports conversational memory, real-time response streaming, and web search for up-to-date information.

### 🚀 Live Demo

👉 **[Try Biddu AI](https://bidduai.streamlit.app/)**

---

## ✨ Features

- 💬 Conversational AI chatbot
- 🧠 Conversation memory using LangGraph `MemorySaver`
- ⚡ Real-time streaming responses
- 🌐 Google Search integration for current information
- 🔄 Maintains conversation context using `thread_id`
- 🎨 Interactive Streamlit interface
- 🤖 Powered by Groq's high-speed inference

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — Frontend & UI
- **LangChain** — LLM integration and tools
- **LangGraph** — Agent workflow and conversation memory
- **Groq** — LLM inference
- **Google Serper** — Web search
- **python-dotenv** — Environment variable management

---

## 🧠 How It Works

```text
User
  │
  ▼
Streamlit Chat Interface
  │
  ▼
LangGraph Agent
  │
  ├──► Groq LLM
  │
  ├──► Google Search
  │
  └──► MemorySaver
          │
          ▼
   Conversation Context
  │
  ▼
Streaming Response
  │
  ▼
User
```

The agent decides when it needs additional information from Google Search and uses `MemorySaver` to maintain conversation context within the same thread.

---

## 📂 Project Structure

```text
Biddu-AI/
│
├── apps/
│   └── personal_chat_bot.py
│
├── notebooks/
│
├── .gitignore
├── requirements.txt
└── imp.txt
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/AbhisheksureshAS/Biddu-AI.git
cd Biddu-AI
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**macOS/Linux**

```bash
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### 5. Run the application

```bash
streamlit run apps/personal_chat_bot.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🔐 Environment Variables

The project uses API keys that should **never be committed to GitHub**.

Required variables:

```text
GROQ_API_KEY
SERPER_API_KEY
```

The `.env` file is excluded through `.gitignore`.

---

## 📌 Future Improvements

- User authentication
- Multiple independent chat sessions
- Persistent database-backed conversation history
- Improved UI and customization
- File/PDF based question answering
- Deployment with persistent memory

---

## 👨‍💻 Author

**Abhishek Suresh**

Built as part of my journey into **Generative AI, LangChain, LangGraph, and AI Agent development**.

### 🌐 Live Project

**[bidduai.streamlit.app](https://bidduai.streamlit.app/)**
