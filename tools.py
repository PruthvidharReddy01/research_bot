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


# -----------------------------------
# Wikipedia Tool
# -----------------------------------
wikipedia_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        top_k_results=3,
        doc_content_chars_max=2000
    )
)


# -----------------------------------
# DuckDuckGo Search Tool
# -----------------------------------
duckduckgo_tool = DuckDuckGoSearchRun()


# -----------------------------------
# Arxiv Research Paper Tool
# -----------------------------------
arxiv_tool = ArxivQueryRun(
    api_wrapper=ArxivAPIWrapper(
        top_k_results=3,
        doc_content_chars_max=2000
    )
)


# -----------------------------------
# Calculator Tool
# -----------------------------------
def calculate(expression: str) -> str:
    """
    Useful for solving mathematical expressions

    Examples:
    - 2 + 2
    - 100 / 5
    - (25 * 4) + 10
    """

    try:
        allowed_chars = "0123456789+-*/(). "

        for char in expression:
            if char not in allowed_chars:
                return "Invalid characters in mathematical expression."

        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation Error: {str(e)}"


calculator_tool = Tool.from_function(
    func=calculate,
    name="Calculator",
    description="""
Useful for solving mathematical calculations.

Examples:
- 2 + 2
- 500 / 10
- (15 * 8) + 20

Only use for mathematical expressions.
"""
)


# -----------------------------------
# Final Tools List
# -----------------------------------
tools = [
    wikipedia_tool,
    duckduckgo_tool,
    arxiv_tool,
    calculator_tool
]