Here’s your **same README style**, but cleanly updated with **RAG as the main highlighted feature** (without changing your tone/structure too much):

---

# Research Bot 🚀

An AI-powered **Hybrid Research ChatBot** built using **Python, LangChain, and Google Gemini API**.

🚀 The core of this project is **Retrieval-Augmented Generation (RAG)** — enabling the chatbot to answer questions using your own documents along with real-time external knowledge.

It helps users perform deep research by combining:

* 📄 Knowledge from uploaded files (RAG)
* 🌐 External tools like Wikipedia, DuckDuckGo, Arxiv
* 🧠 LLM reasoning using Gemini

This project is more than just a chatbot — it is a beginner-friendly step into the world of **AI Agents, Prompt Engineering, RAG Systems, Tool Calling, Structured Output Parsing, and Automation**.

The bot takes a user query, retrieves relevant information from documents, enhances it with tools, structures the response using Pydantic models, and automatically saves the final output into a text file.

---

## ✨ Features

* 📄 **Retrieval-Augmented Generation (RAG) – Core Feature**

  * Answers questions using your own knowledge base
  * Supports multiple file types:

    * `.pdf`, `.docx`, `.txt`, `.csv`, `.xlsx`
  * Uses embeddings + FAISS vector database

* 🌐 External Tools for Better Research

  * Wikipedia Search
  * DuckDuckGo Search
  * Arxiv Research Papers
  * Calculator Tool

* 🧠 Hybrid AI System (RAG + Tools + LLM)

* Prompt Engineering with custom prompt templates

* Structured output using Pydantic

* Automatic parsing and cleanup of LLM responses

* Saves final formatted output into `research_output.txt`

* Beginner-friendly and easy to understand

---

## 🛠 Tech Stack

* Python
* LangChain
* Google Gemini API
* FAISS (Vector Database)
* Pydantic
* DuckDuckGo Search
* Wikipedia API
* Arxiv API
* dotenv

---

## 📂 Project Structure

```bash
research_bot/
│
├── main.py                 # Main chatbot logic (RAG + Tools)
├── rag.py                  # RAG pipeline (multi-file loader + FAISS)
├── tools.py                # Tool definitions
├── documents/              # Your knowledge base (PDF, DOCX, etc.)
├── .env                    # API keys
├── requirements.txt        # Required packages
├── research_output.txt     # Generated output file
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PruthvidharReddy01/research_bot.git
cd research_bot
```

---

### 2. Create Virtual Environment

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

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 📦 requirements.txt

Create a file named `requirements.txt` and add:

```txt
langchain
langchain-core
langchain-community
langchain-google-genai
langchain-classic
langchain-text-splitters
python-dotenv
pydantic
wikipedia
duckduckgo-search
arxiv
faiss-cpu
pypdf
docx2txt
python-docx
openpyxl
pandas
```

Then run:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root folder:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

You can get your Gemini API key from:

**Google AI Studio**

---

## ▶️ Run the Project

```bash
python main.py
```

Example:

```bash
Enter your research query: Summarize my uploaded document
```

---

## 💡 Example Use Cases

### 📄 Document-Based (RAG)

```bash
Summarize my uploaded document
Explain key concepts from my notes
What are the main findings in my file?
```

### 🌐 General Knowledge

```bash
What is Artificial Intelligence?
Explain supply chain optimization
Who is the Prime Minister of India?
```

### 🔥 Hybrid (Best Use Case)

```bash
Compare my uploaded notes with current AI trends
Use my documents and research papers to explain this topic
```

---

## 📄 Output Example

The bot automatically stores results in:

```bash
research_output.txt
```

Example output:

```txt
Topic: Artificial Intelligence

Summary:
Artificial Intelligence (AI) refers to systems that simulate human intelligence...

Sources:
- Wikipedia
- Arxiv
- Internal Documents

Tools Used:
- Wikipedia Tool
- DuckDuckGo Search
```

---

## 🧠 What I Learned

This project helped me understand:

* How AI Agents work behind the scenes
* Prompt Engineering and prompt templates
* Tool Calling with LangChain
* **Retrieval-Augmented Generation (RAG)**
* Vector databases (FAISS)
* Multi-file document processing
* Structured output parsing
* Building real-world AI applications from scratch

This is just the beginning — I plan to build more advanced AI Agents and complex chatbots that solve real-world problems and can potentially grow into startup-level products.

---

## 🔮 Future Improvements

* Add Memory to the chatbot
* Persistent vector database (avoid recomputation)
* PDF report generation
* Web UI using Streamlit or React
* Multi-Agent workflow
* Database storage
* User authentication
* Advanced research summarization
* Startup-ready production version

---

## 🤝 Contributing

Contributions are always welcome.

Feel free to fork the project, improve it, and submit a pull request.

---

## 📌 GitHub Repository

[https://github.com/PruthvidharReddy01/research_bot.git](https://github.com/PruthvidharReddy01/research_bot.git)

---

## ⭐ Final Note

AI Agents + RAG systems are the future.

This project may look simple — but it represents a powerful concept of combining:

👉 **LLMs + Tools + Knowledge Bases**

Small project today.
Bigger vision tomorrow. 🚀
