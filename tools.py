from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

tool=TavilySearch(max_results=3)
result =tool.invoke("What is langgraph?")
print(result)

## Custom function
def multiply(a:int,b:int)->int:
    """Multiply a and b

    Args:
        a (int): first int
        b (int): second int

    Returns:
        int: output int
    """
    return a*b