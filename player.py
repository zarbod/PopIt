class Player:

    def __init__(self, turn=None):
        self.score = 0
        self.turn = turn

    def set_turn(self, turn_bool):
        self.turn = turn_bool

    def get_score(self):
        return self.score

    def set_score(self, s):
        self.score = s




