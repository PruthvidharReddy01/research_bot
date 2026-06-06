# Slack Research Analytics Bot 🚀

An AI-powered **Slack-integrated Research Analytics Assistant** built using **Python, LangChain, Google Gemini, FAISS, Slack API, and Google Calendar API**.

The project combines:

* 📄 Retrieval-Augmented Generation (RAG)
* 🌐 External Research Tools
* 💬 Slack Workspace Integration
* 📅 Google Calendar Automation
* 🎥 Automatic Google Meet Generation

Users can upload documents directly in Slack, analyze meeting transcripts, perform research, extract business insights, and schedule meetings without leaving Slack.

---

## ✨ Features

### 📄 Retrieval-Augmented Generation (RAG)

* Uses uploaded documents as a knowledge base
* Supports:

  * PDF
  * DOCX
  * TXT
  * CSV
  * XLSX
* FAISS Vector Database
* Semantic Retrieval using Gemini Embeddings

### 📊 Research Analytics

* Document Summarization
* Meeting Transcript Analysis
* Business Insight Extraction
* Action Item Identification
* Key Decision Extraction
* Executive Summaries

### 🌐 External Research Tools

* Wikipedia Search
* DuckDuckGo Search
* Calculator Tool

### 💬 Slack Integration

* Mention-based interaction
* Slack File Upload Support
* Automatic Document Ingestion
* Workspace User Discovery
* Real-time Research Assistance

### 📅 Meeting Scheduling

The bot can schedule meetings directly from Slack.

Example:

@Bot Schedule a meeting with Marc tomorrow at 4pm

Features:

* Natural Language Scheduling
* Attendee Extraction
* Email Discovery from Slack Workspace
* Date & Time Parsing
* Google Calendar Event Creation
* Automatic Invitation Sending
* Google Meet Link Generation

### 🎯 Intelligent Topic Extraction

Example:

@Bot Schedule a meeting with Marc about Q4 Planning on June 15th at 10am

Automatically extracts:

* Attendee: Marc
* Topic: Q4 Planning
* Date: June 15th
* Time: 10:00 AM

The topic becomes the Google Calendar event title.

---

## 🛠 Tech Stack

* Python
* LangChain
* Google Gemini API
* FAISS Vector Database
* Slack Bolt SDK
* Flask
* Google Calendar API
* Google OAuth
* DuckDuckGo Search
* Wikipedia API
* Pydantic
* DateParser
* dotenv

---

## 📂 Project Structure

research_bot/

├── main.py

├── rag.py

├── tools.py

├── meeting.py

├── calendar_service.py

├── documents/

├── uploaded_docs/

├── requirements.txt

├── README.md

└── .env

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/PruthvidharReddy01/research_bot.git

cd research_bot

### Create Virtual Environment

Windows

python -m venv venv

venv\Scripts\activate

Linux / Mac

python3 -m venv venv

source venv/bin/activate

### Install Requirements

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file:

GOOGLE_API_KEY=

SLACK_BOT_TOKEN=

SLACK_SIGNING_SECRET=

---

## 📅 Google Calendar Setup

1. Create a Google Cloud Project
2. Enable Google Calendar API
3. Create OAuth Desktop Credentials
4. Download credentials.json
5. Place credentials.json in the project root
6. Authenticate once to generate token.pickle

---

## 💬 Slack Setup

Required OAuth Scopes:

* app_mentions:read
* chat:write
* files:read
* users:read
* channels:history

Enable Event Subscriptions:

* app_mention

Install the app into your workspace.

---

## ▶️ Run the Project

python main.py

---

## 💡 Example Commands

### Research

@Bot Summarize this uploaded transcript

@Bot Give meaningful insights from the Q3 meeting

@Bot What are the key decisions made in this document?

### Meeting Scheduling

@Bot Schedule a meeting with Marc tomorrow at 4pm

@Bot Schedule a meeting with Marc about Revenue Planning on June 15th at 10am

---

## 📌 Example Meeting Response

Meeting Created

Topic: Revenue Planning

Name: Marc

Email: [marc@example.com](mailto:marc@example.com)

Time: 2026-06-15 10:00:00

Meet Link:

https://meet.google.com/xxxx-xxxx-xxx

---

## 🏗 System Architecture

Slack User

↓

Slack App

↓

Intent Detection

↓

Research Workflow OR Meeting Workflow

↓

Gemini + RAG + Tools

↓

Google Calendar (if scheduling)

↓

Google Meet Generation

↓

Slack Response

---

## 🔮 Future Improvements

* Automatic Meeting Agenda Generation
* Follow-up Meeting Scheduling from Transcripts
* Multi-attendee Scheduling
* Persistent Vector Database
* Memory-enabled Conversations
* Multi-Agent Workflows
* React Dashboard
* Production Deployment

---

## 🧠 What I Learned

This project helped me understand:

* AI Agents
* Prompt Engineering
* Tool Calling
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Slack API Integration
* Google Calendar Automation
* Google Meet Generation
* Document Intelligence Systems
* Real-world AI Application Development

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests.

---

## ⭐ Final Note

This project combines:

👉 LLMs + RAG + Tools + Slack + Google Calendar + Google Meet

to create an AI-powered workplace assistant capable of research, analytics, document intelligence, and meeting automation.

Small project today.

Bigger vision tomorrow. 🚀
