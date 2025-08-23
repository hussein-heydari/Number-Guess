class Score:
    def __init__(self):
        self.score = 10
    def penalty(self):
        if self.score == 1:
            return None
        else:
            self.score -= 1
