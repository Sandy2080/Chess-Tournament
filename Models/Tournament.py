from tinydb import TinyDB, Query, where
from datetime import datetime, timedelta

from Models.Round import Round
class Tournament:
    """Tournoi d'échec."""

    def __init__(self):
        """Initialize an instance of Tournament """
        self.tournament_id = 0
        self.name = ""
        self.location = ""
        self.starting_date = ""
        self.ending_date = ""
        self.current_round = 0,
        self.rounds_total = 4,
        self.players = []
        self.description = ""

    def serialize(self):
        """ Converts to JSON format """
        return {
            "tournament_id": self.tournament_id,
            "name": self.name,
            "location": self.location,
            "starting_date": self.starting_date,
            "ending_date": self.ending_date,
            "rounds_total": 4,
            "current_round": 0,
            "players": [],
            "description": self.description
        }

    def toObject(self, informations: dict):
        """ Converts to Tournament object """
        print(informations)
        self.tournament_id = informations["tournament_id"]
        self.name = informations["name"]
        self.location = informations["location"]
        self.starting_date = informations["starting_date"]
        self.ending_date = informations["ending_date"]
        self.description = informations["description"]
        self.rounds_total = 4
        self.current_round = 0
        self.players = []

    def save_tournament_to_db(self, informations, pairs):
        """Save new tournament to database """
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        round_id = len(Round.load_round_db()) + 1
        tournaments_db.insert({
            "tournament_id": informations["tournament_id"],
            "name": informations["name"],
            "location": informations["location"],
            "starting_date": informations["starting_date"],
            "ending_date": informations["ending_date"],
            "rounds_total": 4,
            "current_round": round_id,
            "description": informations["description"],
            "players": pairs,
        })
        return informations["tournament_id"]

    @staticmethod
    def load_tournament_db():
        """Save new tournament to database """
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        return tournaments_db.all()

    @staticmethod
    def update_tournament_db(tournament_id, round_id):
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        tournament = Query()
        tournaments_db.update({"current_round": round_id}, tournament.tournament_id == tournament_id)

    def save_round_to_db(self, tournament_id, pairs):
        """Save new player to database """
        tournaments = self.load_tournament_db()
        tournament = tournaments[tournament_id - 1]
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        round_id = len(rounds_db.all()) + 1
        round_id = rounds_db.insert({
            "tournament_id": tournament_id,
            "round_id": round_id,
            "starting_date": tournament["starting_date"],
            "starting_time":  datetime.now().strftime("%H:%M"),
            "ending_time":  (datetime.now() + timedelta(minutes=30)).strftime("%H:%M"),
            "pairs": pairs
        })
        return round_id

