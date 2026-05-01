from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_react_agent, AgentExecutor

from tools import tools
from rag import create_vectorstore

import json
import re

load_dotenv(override=True)

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

parser = PydanticOutputParser(
    pydantic_object=ResearchResponse
)

# RAG: Created vector to store
vectorstore = create_vectorstore()

if vectorstore:
    retriever = vectorstore.as_retriever()
else:
    retriever = None

react_prompt = PromptTemplate.from_template(
    """
You are an advanced AI Research Assistant.

Your job is to answer user questions in depth using:

1. External tools (Wikipedia, DuckDuckGo, Arxiv, Calculator)
2. Internal knowledge base from uploaded files (RAG)

You must:
- provide detailed explanations
- use examples where needed
- explain practical applications
- mention important insights
- provide reliable sources
- use tools whenever necessary
- use RAG context whenever relevant

RAG Context:
{rag_context}

Available tools:

{tools}

Use this exact format:

Question: the question to answer
Thought: think carefully
Action: the tool to use, should be one of [{tool_names}]
Action Input: input for the tool
Observation: result of the tool
... (this can repeat multiple times)
Thought: I now know the final answer

Final Answer:
{format_instructions}

Question: {input}
Thought:{agent_scratchpad}
"""
).partial(
    format_instructions=parser.get_format_instructions()
)

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

query = input("Enter your research query: ")

# RAG: Retrieve relevant context
rag_context = "No document context available."

if retriever:
    try:
        relevant_docs = retriever.invoke(query)

        if relevant_docs:
            rag_context = "\n\n".join(
                [doc.page_content for doc in relevant_docs[:3]]
            )

    except Exception as e:
        rag_context = f"RAG Error: {str(e)}"

response = agent_executor.invoke(
    {
        "input": query,
        "rag_context": rag_context
    }
)

raw_output = response["output"]

print("\nFinal Response:\n")
print(raw_output)

def clean_text(text):
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    return cleaned.strip()

cleaned_output = clean_text(raw_output)
parsed_response = None

try:
    parsed_response = parser.parse(cleaned_output)

except Exception:
    try:
        parsed_response = ResearchResponse(
            **json.loads(cleaned_output)
        )
    except Exception:
        parsed_response = None

with open("research_output.txt", "w", encoding="utf-8") as file:

    if parsed_response:

        file.write(f"Topic: {parsed_response.topic}\n\n")

        file.write(f"Summary:\n{parsed_response.summary}\n\n")

        file.write("Sources:\n")
        for source in parsed_response.sources:
            file.write(f"- {source}\n")

        file.write("\nTools Used:\n")
        for tool in parsed_response.tools_used:
            file.write(f"- {tool}\n")

    else:
        file.write("Could not parse structured output.\n\n")
        file.write(raw_output)

print("\nSaved to research_output.txt successfully")