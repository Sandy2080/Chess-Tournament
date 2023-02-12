class Round:
    """Tour d'échec."""

    def __init__(self, _number, _starting_date, _ending_date, _starting_time, _ending_time):
        """Initialise les modalités du tournoi"""
        self.name = "Round " + str(_number)
        self.starting_date = _starting_date
        self.starting_time = _starting_time
        self.ending_date = _ending_date
        self.ending_time = _ending_time
        self.matches = []

    def make_pairs(self, _round):
        # self.matches.append(_round)
        print("save to db")
    
    def save_match(self, pairs):
        self.matches.append(_round)
        print("save to db")


       