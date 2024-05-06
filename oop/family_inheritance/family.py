from typing import List


class Parent:
    hair: str
    languages: List[str]
    
    def __init__(self) -> None:
        self.hair = 'brown'
        self.languages = ['english']
        
    
class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.languages.append('cantonese')
