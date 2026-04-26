from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_react_agent, AgentExecutor
from tools import tools
import json
import re

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",#used for cost effective since all the other models are very expensive using credits, you can change it to any other model if you want.
)

parser = PydanticOutputParser(
    pydantic_object=ResearchResponse
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate a research paper.
            Answer the user query clearly.
            Wrap the output in this format and provide no other text.

            {format_instructions}
            """
        ),
        ("human", "{query}")
    ]
).partial(
    format_instructions=parser.get_format_instructions()
)

react_prompt = PromptTemplate.from_template(
    """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: {format_instructions}

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
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

response = agent_executor.invoke(
    {"input": input("Enter your research query: ")}
)

raw_output = response["output"]
print(raw_output)


def clean_text(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\s*```$", "", cleaned, flags=re.MULTILINE)
    return cleaned.strip()

cleaned_output = clean_text(raw_output)
parsed_response = None

try:
    parsed_response = parser.parse(cleaned_output)
except Exception:
    try:
        parsed_response = ResearchResponse(**json.loads(cleaned_output))
    except Exception:
        parsed_response = None

output_file = "research_output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    if parsed_response is not None:
        f.write(f"Topic: {parsed_response.topic}\n\n")
        f.write(f"Summary:\n{parsed_response.summary}\n\n")
        f.write("Sources:\n")
        for source in parsed_response.sources:
            f.write(f"- {source}\n")
        f.write("\nTools Used:\n")
        for tool in parsed_response.tools_used:
            f.write(f"- {tool}\n")
    else:
        f.write("Could not parse structured output. Raw output below:\n\n")
        f.write(raw_output)

print(f"Saved structured output to {output_file}")