from tinydb import TinyDB, Query

class Player:
    """Joueur d'échec."""
    
    def __init__(self, _id, _first, _last, _dob, _score):
        """Initialise les informations de chaque joueur"""
        self.id = _id
        self.first = _first
        self.last = _last
        self.dob = _dob
        self.score = _score

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self._id,
            "last": self._last,
            "first": self._first,
            "dob": self._dob,
            "score": self._score
        }

    def __str__(self):
        """Retourne une instance de player."""
        return f"New player {self.first}, {self.last}."

    @staticmethod
    def load_player_db():
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players