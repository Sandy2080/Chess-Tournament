from tinydb import TinyDB

class Round:
    """Tour d'échec."""

    def __init__(self, number: int, starting_date: str, ending_date: str, starting_time: str, ending_time: str, players: list):
        """Initialise les modalités du tournoi"""
        self.id = number
        self.name = "Round " + str(number)
        self.starting_date = starting_date
        self.starting_time = starting_time
        self.ending_date = ending_date
        self.ending_time = ending_time
        self.players = players
        self.matches = []

    def make_pairs(self, round):
        print("save to db")
    
    def save_match(self, pairs):
        print("save to db")


       