
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

    def __str__(self):
        """Retourne une instance de player."""
        return f"New player {self.first}, {self.last}."