from dataclasses import dataclass


@dataclass
class VotingStation:
    voters: dict[str, bool]
    
    def cast_vote(self, name: str) -> str:
        if self.voters.get(name):
            return f'{name} already voted'
        
        self.voters[name] = True
        return f'{name} just voted'
