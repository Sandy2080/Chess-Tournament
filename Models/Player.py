from tinydb import TinyDB

class Player:
    """Joueur d'échec."""
    
    def __init__(self, first: str, last: str, dob: str, score: int):
        """Initialise les informations de chaque joueur"""
        self.id = 0
        self.first = first
        self.last = last
        self.dob = dob
        self.score = score

    def serialize_player(self):
        """Return serialized player info"""
        return {
            "id": self.player_id,
            "last": self.last,
            "first": self.first,
            "dob": self.dob,
            "score": self.score
        }

    def save_to_db(self):
        """Save new player to database """
        players_db = TinyDB('data/players.json')
        players_db.all()
        player_id = len(players_db.all()) + 1
        player_id = players_db.insert({
            "id": player_id,
            "last": self.last,
            "first": self.first,
            "dob": self.dob,
            "score": self.score,
            "score": 0
        })
        print("new player " + self.first +","+ self.last + " successfully saved")

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
    
    def __str__(self):
        """Retourne une instance de player."""
        return f"New player {self.first}, {self.last}."