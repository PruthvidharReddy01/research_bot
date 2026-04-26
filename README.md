# Research Bot 🚀

An AI-powered **Research ChatBot** built using **Python, LangChain, and Google Gemini API** that helps users perform quick research using multiple tools like Wikipedia, DuckDuckGo, Arxiv, and a Calculator.

This project is more than just a chatbot — it is a beginner-friendly step into the world of **AI Agents, Prompt Engineering, Tool Calling, Structured Output Parsing, and Automation**.

The bot takes a user query, performs research using available tools, structures the response using Pydantic models, and automatically saves the final output into a text file for future reference.

---

## ✨ Features

* AI-powered research assistant using Gemini API
* Uses multiple tools for better answers:

  * Wikipedia Search
  * DuckDuckGo Search
  * Arxiv Research Papers
  * Calculator Tool
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
├── main.py                 # Main chatbot logic
├── tools.py                # Tool definitions
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
python-dotenv
pydantic
wikipedia
duckduckgo-search
arxiv
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
Enter your research query: Who is the Prime Minister of India?
```

---

## 📄 Output Example

The bot automatically stores results in:

```bash
research_output.txt
```

Example output:

```txt
Topic: Prime Minister of India

Summary:
Narendra Modi is the Prime Minister of India...

Sources:
- Wikipedia
- DuckDuckGo

Tools Used:
- Wikipedia Tool
- Search Tool
```

---

## 🧠 What I Learned

This project helped me understand:

* How AI Agents work behind the scenes
* Prompt Engineering and prompt templates
* Tool Calling with LangChain
* Structured output parsing
* Response cleaning and reliability improvement
* Building real-world AI applications from scratch

This is just the beginning — I plan to build more advanced AI Agents and complex chatbots that solve real-world problems and can potentially grow into startup-level products.

---

## 🔮 Future Improvements

* Add Memory to the chatbot
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

AI Agents are the future.

This project may be simple, but it represents a much bigger vision — building intelligent systems that can help people, automate work, and create real impact.

Small project today.
Bigger vision tomorrow. 🚀
