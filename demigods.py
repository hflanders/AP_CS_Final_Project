class Demigods:

    def __init__(self, percy: int, annabeth: int, grover: int):
        self.leaders = {
            'percy': percy,
            'annabeth': annabeth,
            'grover': grover
        }

    def add(self,leaders: str) -> None:
        if leaders == 'percy':
            self.leaders['percy'] = self.leaders.get('percy') + 1
        if leaders == 'annabeth':
            self.leaders['annabeth'] = self.leaders.get('annabeth') + 1
        if leaders == 'grover':
            self.leaders['grover'] = self.leaders.get('grover') + 1

    def select(self) -> str:
        score = 0
        result = ''
        for leaders, points in self.leaders.items():
            if points > score:
                result = leaders
                
        return result
    
    def clear(self) -> None:
        self.leaders = {
            'percy': 0,
            'annabeth': 0,
            'grover': 0
        }