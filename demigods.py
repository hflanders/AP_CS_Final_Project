import random

class Demigods:

    def __init__(self, percy : int, annabeth: int, grover: int, nico: int, thalia: int):
        self.leaders = {
            'Percy Jackson': percy,
            'Annabeth Chase': annabeth,
            'Grover Underwood': grover,
            'Nico Di Angelo': nico,
            'Thalia Grace': thalia
        }

    def add(self,leaders: str) -> None:
        if leaders == 'Percy Jackson':
            self.leaders['Percy Jackson'] = self.leaders.get('percy') + 1
        if leaders == 'Annabeth Chase':
            self.leaders['Annabeth Chase'] = self.leaders.get('annabeth') + 1
        if leaders == 'Grover Underwood':
            self.leaders['Grover Underwood'] = self.leaders.get('grover') + 1
        if leaders == 'Nico Di Angelo':
            self.leaders['Nico Di Angelo'] = self.leaders.get('nico') + 1
        if leaders == 'Thalia Grace':
            self.leaders['Thalia Grace'] = self.leaders.get('thalia') + 1

    def select(self) -> str:
        score = 0
        result = ''
        ties = []
        for leader, points in self.leaders.items():
            if points > score:
                result = leader
                score = points
            elif points == score:
                ties.append(leader)

        if len(ties) == 0:
            return result
        
        return ties[random.randint(0,len(ties)-1)]
    
    def clear(self) -> None:
        self.leaders = {
            'Percy Jackson': 0,
            'Annabeth Chase': 0,
            'Grover Underwood': 0,
            'Nico Di Angelo': 0,
            'Thalia Grace': 0
        }