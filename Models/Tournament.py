from tinydb import TinyDB
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

    @staticmethod
    def load_tournament_db() -> list:
        """Load tournaments database
        @return: list of tournaments
        """
        tournaments_db = TinyDB('data/tournaments.json')
        tournaments_db.all()
        tournaments = []
        for item in tournaments_db:
            tournaments.append(item)

        return tournaments

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
      