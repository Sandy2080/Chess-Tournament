from tinydb import TinyDB


class Round:
    """Tour d'échec."""

    def __init__(self):
        """Initialise les modalités du tournoi"""
        self.id = 0
        self.name = ""
        self.starting_date = ""
        self.starting_time = ""
        self.ending_date = ""
        self.ending_time = ""
        self.players = []
        self.matches = []

    def load_round_db():
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        return rounds_db.all()

    def load_last_round(self):
        """Load rounds database
        @return: list of rounds
        """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        all_rounds = rounds_db.all()
        return all_rounds[-1]

    @staticmethod
    def load_pairs():
        """Load rounds database
        @return: list of rounds
        """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        all_rounds = rounds_db.all()
        _round = all_rounds[-1]
        return _round["pairs"]
