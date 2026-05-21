# Slack Integrated Research Bot 🚀

An AI-powered **Hybrid Research & Reasoning ChatBot** built using **Python, LangChain, Google Gemini API, RAG, and Slack Integration**. 

🚀 The core of this project is **Retrieval-Augmented Generation (RAG)** combined with a **tool-using AI reasoning agent** — enabling the chatbot to answer questions using:

* 📄 Internal knowledge bases and uploaded files
* 🌐 Real-time external web research
* 🧠 LLM reasoning and tool calling
* 💬 Slack workspace integration

This is not just a normal chatbot.

The bot acts like an **AI Research Assistant** that can:

* think step-by-step,
* use tools when necessary,
* retrieve information from uploaded company documents,
* search the web for live information,
* reason over both together,
* and provide structured research-style outputs.

The system is heavily inspired by modern AI agent architectures like:

* ChatGPT Deep Research
* Perplexity AI
* Enterprise Slack AI Assistants
* RAG-based copilots

---

# ✨ Features

## 📄 Retrieval-Augmented Generation (RAG)

The bot can answer questions using your own knowledge base.

Supports:

* `.pdf`
* `.docx`
* `.txt`
* `.csv`
* `.xlsx`

Uses:

* embeddings
* chunking
* FAISS vector database
* semantic retrieval

---

## 💬 Slack Workspace Integration

The chatbot is fully integrated into Slack.

Users can:

* mention the bot directly,
* ask research questions,
* upload PDFs/documents,
* and receive AI-generated responses inside Slack channels.

### Slack Features

* Slack bot integration
* Real-time event handling
* File upload support
* Automatic PDF/document ingestion
* Instant RAG refresh after uploads
* Enterprise-style AI assistant workflow

---

## 🌐 External Research Tools

The AI agent can dynamically use external tools:

* Wikipedia Search
* DuckDuckGo Search
* Arxiv Research Papers
* Calculator Tool

This creates a hybrid reasoning system that combines:

* internal company knowledge
* external internet knowledge
* AI reasoning

---

## 🧠 AI Reasoning Agent (ReAct Agent)

The project uses a **ReAct-style AI agent**.

The bot can:

* think step-by-step,
* decide when tools are needed,
* search external sources,
* retrieve internal knowledge,
* combine information,
* and generate structured outputs.

This is much more advanced than a basic chatbot.

---

## 📦 Structured Output Generation

Uses:

* Pydantic
* output parsing
* automatic response cleanup

The final response is:

* structured,
* formatted,
* and saved automatically.

---

## 📂 Automatic Knowledge Base System

Uploaded Slack documents are:

1. downloaded automatically,
2. stored locally,
3. converted into embeddings,
4. indexed into FAISS,
5. instantly available for RAG retrieval.

No manual retraining required.

---

# 🛠 Tech Stack

* Python
* LangChain
* Google Gemini API
* FAISS Vector Database
* Flask
* Slack Bolt SDK
* Pydantic
* DuckDuckGo Search
* Wikipedia API
* Arxiv API
* dotenv

---

# 📂 Project Structure

```bash
research_bot/
│
├── main.py                 # Main AI agent + Slack integration
├── rag.py                  # RAG pipeline + FAISS vectorstore
├── tools.py                # Tool definitions
├── documents/              # Static knowledge base
├── uploaded_docs/          # Slack uploaded files
├── .env                    # API keys & Slack secrets
├── requirements.txt
├── research_output.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/PruthvidharReddy01/research_bot.git
cd research_bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

```txt
langchain
langchain-core
langchain-community
langchain-classic
langchain-google-genai
langchain-text-splitters

python-dotenv
pydantic

wikipedia
duckduckgo-search
ddgs
arxiv

faiss-cpu
tiktoken

pypdf
docx2txt
python-docx
openpyxl
pandas
unstructured

flask
slack_bolt
requests
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key

SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_SIGNING_SECRET=your_slack_signing_secret
```

---

# 💬 Slack Setup

## Create Slack App

Go to:

[Slack API Apps Dashboard](https://api.slack.com/apps?utm_source=chatgpt.com)

Create a new app.

---

## Required OAuth Scopes

Add these Bot Token Scopes:

```text
app_mentions:read
chat:write
files:read
channels:history
```

Then:

* Install/Reinstall app to workspace

---

## Event Subscriptions

Enable Events.

Set Request URL:

```text
https://YOUR-NGROK-URL/slack/events
```

Add Bot Event:

```text
app_mention
```

---

# 🌍 ngrok Setup

Since Slack needs a public URL to communicate with your local machine, ngrok is used as a tunnel.

Download ngrok:

[Ngrok Official Website](https://ngrok.com?utm_source=chatgpt.com)

Run:

```bash
ngrok http 3000
```

Example:

```text
https://abcd1234.ngrok-free.app
```

Use:

```text
https://abcd1234.ngrok-free.app/slack/events
```

inside Slack Event Subscriptions.

---

# ▶️ Run The Project

## Start Bot Server

```bash
python main.py
```

---

## Start ngrok

```bash
ngrok http 3000
```

---

# 💡 Example Use Cases

## 📄 Document Research

```text
@ResearchBot summarize this PDF
```

```text
@ResearchBot explain the key insights from this meeting transcript
```

---

## 🌐 Web Research

```text
@ResearchBot latest AI trends in supply chain
```

---

## 🔥 Hybrid Research (Best Feature)

```text
@ResearchBot compare my uploaded document with current AI trends
```

```text
@ResearchBot analyze this company transcript and provide market insights
```

---

# 🧠 Architecture Flow

```text
Slack User
   ↓
Slack Event
   ↓
ngrok Tunnel
   ↓
Flask Server
   ↓
Slack Bolt
   ↓
AI Agent
   ↓
RAG Retrieval
   ↓
Tool Calling
   ↓
Gemini Reasoning
   ↓
Structured Response
   ↓
Slack Reply
```

---

# 📄 Output Example

```text
Topic: Strategic Performance Review

Summary:
The company demonstrated strong revenue growth but faced increasing infrastructure costs...

Sources:
• Internal Meeting Transcript
• Wikipedia
• Arxiv
```

---

# 🧠 What I Learned

This project helped me understand:

* AI Agents
* Prompt Engineering
* Tool Calling
* RAG Systems
* Vector Databases
* Semantic Search
* Slack API Integration
* Event-driven systems
* Webhooks
* Flask servers
* ngrok tunneling
* Structured output parsing
* Enterprise AI assistant architecture

This project evolved from a simple RAG chatbot into a more advanced:

* reasoning AI system,
* research assistant,
* and Slack-integrated enterprise-style AI agent.

---

# 🔮 Future Improvements

* Memory-enabled conversations
* Persistent vector database
* ChromaDB integration
* Multi-agent workflows
* Voice support
* React/Next.js frontend
* Authentication system
* Cloud deployment
* Streaming responses
* Citation system
* Autonomous research workflows

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the project, improve it, and submit pull requests.

---

# 📌 GitHub Repository

[Research Bot GitHub Repository](https://github.com/PruthvidharReddy01/research_bot?utm_source=chatgpt.com)

---

# ⭐ Final Note

This project combines:

👉 **LLMs + RAG + Tool Calling + Slack Integration + Knowledge Bases**

to create a modern AI-powered research assistant.

Small project today.
Much bigger vision tomorrow. 🚀
