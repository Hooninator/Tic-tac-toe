class Square:
    def __init__(self, coordinates=None):
        self.contents=None
        self.coordinates=coordinates
    def fill_square(self, symbol):
        self.contents = symbol

class Game:
    def __init__(self, active_player=None, turns=0):
        self.turns = turns
        self.active = active_player


    