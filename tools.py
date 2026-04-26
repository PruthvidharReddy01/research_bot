from langchain_community.tools import (
    WikipediaQueryRun,
    DuckDuckGoSearchRun,
    ArxivQueryRun,
)
from langchain_community.utilities import (
    WikipediaAPIWrapper,
    ArxivAPIWrapper,
)
from langchain_core.tools import Tool

# Initialize tools
wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
duckduckgo_tool = DuckDuckGoSearchRun()
arxiv_tool = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())

def calculate(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

calculator_tool = Tool.from_function(
    func=calculate,
    name="Calculator",
    description="Useful for calculating mathematical expressions."
)

tools = [
    wikipedia_tool,
    duckduckgo_tool,
    arxiv_tool,
    calculator_tool,
]