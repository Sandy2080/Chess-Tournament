from tinydb import TinyDB, Query, where


class Player:
    """Joueur d'échec."""

    def __init__(self, first: str, last: str, genre: str, dob: str, score: int):
        """Initialise les informations de chaque joueur"""
        self.id = 0
        self.first = first
        self.last = last
        self.dob = dob
        self.genre = genre
        self.score = score

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self.player_id,
            "last": self.last,
            "first": self.first,
            "dob": self.dob,
            "genre": self.genre,
            "score": self.score
        }

    @staticmethod
    def insert_player_to_db(player):
        """Save new player to database """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        players_db.all()
        player_id = len(players_db.all()) + 1
        players_db.insert({
            "id": player_id,
            "last":  player["last"],
            "first": player["first"],
            "dob": player["dob"],
            "score": 0,
        })

    @staticmethod
    def load_players_db():
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json')
        _all = players_db.all()
        players = []
        for item in _all:
            players.append(item)
        return players

    @staticmethod
    def remove_records(players):
        players_db = TinyDB('data/players.json')
        for player in players:
            players_db.remove(where('first') == player["first"])
        return players_db.all()

    @staticmethod
    def update_player_score(player):
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        q = Query()
        players_db.update({"score": player["score"]}, q.id == player["id"])

    def __str__(self):
        """Retourne une instance de player."""
        return f"New player {self.first}, {self.last}."
