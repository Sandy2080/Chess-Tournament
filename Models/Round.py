from tinydb import TinyDB

class Round:
    """Tour d'échec."""

    def __init__(self, number: int, starting_date: str, ending_date: str, starting_time: str, ending_time: str, players: list):
        """Initialise les modalités du tournoi"""
        self.name = "Round " + str(number)
        self.starting_date = starting_date
        self.starting_time = starting_time
        self.ending_date = ending_date
        self.ending_time = ending_time
        self.players = players
        self.matches = []

    @staticmethod
    def load_round_db():
        """Load rounds database
        @return: list of rounds
        """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        rounds_db.all()
        rounds = []
        for item in rounds_db:
            rounds.append(item)
        return rounds

    def insert_to_db(self, tournament):
        """Save new player to database """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        rounds_db.all()
        round_id = len(rounds_db.all()) + 1
        round_id = rounds_db.insert({
            "tournament_id": tournament.tournament_id,
            "round_id": round_id,
            "name": self.name,
            "starting_date": self.starting_date,
            "ending_date": self.ending_date,
            "starting_time": self.starting_time,
            "ending_time": self.ending_time,
            "players": self.players
        })
        print("New Round: " + self.name +" starting on " + self.starting_date + " successfully saved")


    def make_pairs(self, round):
        print("save to db")
    
    def save_match(self, pairs):
        print("save to db")


       