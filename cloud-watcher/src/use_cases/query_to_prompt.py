from typing import Protocol
from src.domain.user_query import Query
from langchain.prompts import HumanMessagePromptTemplate

LANGCHAIN_PROMPT = """Context: {context}. Question: {query}"""

# convert input query into prompts for LLM
class QueryPrompter(Protocol):
    query: Query
    
    def create_prompt(self, *args, **kwargs):
        ...

class LangChainQPrompter:
    def __init__(self, query:Query) -> None:
        self.query = query
    
    def create_prompt(self, template:str):
        return HumanMessagePromptTemplate.from_template(template)