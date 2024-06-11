import random

class Demigods:
    """Creates a class for all the characters involved in this quiz"""

    def __init__(self, percy : int, annabeth: int, grover: int, nico: int, thalia: int):
        self.leaders = {
            'Percy Jackson': percy,
            'Annabeth Chase': annabeth,
            'Grover Underwood': grover,
            'Nico Di Angelo': nico,
            'Thalia Grace': thalia
        }

    def add(self,leaders: str) -> None:
        # is the way to track and add points to the characters as their answers are selected
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
        # selects the character who has the most points, and if there is a tie randomly selects one of the characters who are tied
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
        
        # check for distinct max
        max = 0
        max_leader = ''
        for leader, points in self.leaders.items():
            if points > max:
                max = points
                max_leader = leader

        # check if max is unique
        count = 0
        for leader, points in self.leaders.items():
            if points == max:
                count += 1

        # there's a distinct max
        if count == 1:
            return max_leader
        
        return ties[random.randint(0,len(ties)-1)]
    
    def clear(self) -> None:
        # clears the points we collected during the playthrough of our quiz
        self.leaders = {
            'Percy Jackson': 0,
            'Annabeth Chase': 0,
            'Grover Underwood': 0,
            'Nico Di Angelo': 0,
            'Thalia Grace': 0
        }