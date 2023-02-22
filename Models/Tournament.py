from tinydb import TinyDB, Query

class Tournament:
    """Tournoi d'échec."""

    def __init__(self):
        """Initialise les modalités du tournoi"""
        self.tournament_id = 0
        self.name = ""
        self.location = ""
        self.starting_date = ""
        self.ending_date = ""
        self.current_round = 0
        self.players = []
        self.description = ""

    @staticmethod
    def load_tournament_db():
        """Load tournaments database
        @return: list of tournaments
        """
        tournaments_db = TinyDB('data/tournaments.json')
        tournaments_db.all()
        tournaments = []
        for item in tournaments_db:
            tournaments.append(item)

        return tournaments

    def create(self, name, location, starting_date, ending_date,  description):
        """Renseigne les modalités du tournoi"""
        self.tournament_id = 0
        self.name = name
        self.location = location
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.current_round = 0
        self.players = []
        self.description = description

    def increment_round(self):
        self.current_round < self.getRounds_total()
        self.current_round += 1

    def getRounds_total(self):
        return 4
 

    def describe(self):
        tournaments_db = TinyDB('data/tournaments.json')
        last_tournament = tournaments_db.all()[-1]
        players = len(last_tournament["players"])
        print("\n" * 3 + "--- NEW TOURNAMENT ---")
        print("***Tournament started :" +  last_tournament["name"].upper() + "***")
        print("-ID: "+ str(last_tournament["id"]))
        print("-Date: "+ last_tournament["starting_date"])
        print("-Location : "+ last_tournament["location"])
        print("-Rounds : "+ str(last_tournament["rounds"]))
        print("-Current round : "+ str(last_tournament["current_round"]))
        print("-Number of players : "+ str(players))

    def select_randomly(self):
        pass
    

