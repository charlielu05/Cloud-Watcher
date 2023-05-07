from typing import Protocol

class Query(Protocol):
    raw_input:str
    
    def get_input(self)->None:
        ...

    def return_input(self)->str:
        ...

class CLIQuery:
    def __init__(self, raw_input="", cleansed_input="") -> None:
        self.raw_input = raw_input
        self.cleansed_input = cleansed_input
    
    def _clean_input(self)->None:
        self.cleansed_input = self.raw_input.strip()
            
    def get_query(self)->None:
        self.raw_input = input()
        
    def return_query(self)->str:
        self._clean_input()
        return self.cleansed_input