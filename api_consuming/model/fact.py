class Fact:

    def __init__(self, fact):
        self.fact = fact

    def __str__(self) -> str:
        return f"Here it goes a Fun Fact about Cats: {self.fact}"
    
    def get_fact(self):
        return self.fact

class FactConverter:

    def convert(self, fact) -> Fact:
        new_fact = fact['fact']
        return Fact(new_fact)