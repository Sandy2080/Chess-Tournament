from tinydb import TinyDB

class Tournament:
    """Tournoi d'échec."""

    def __init__(self, name, location, starting_date, ending_date,  description):
        """Initialise les modalités du tournoi"""
        self.tournament_id = 0
        self.name = name
        self.location = location
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.current_round = 0
        self.players = []
        self.description = description
    
    @staticmethod
    def getRounds_total():
        return 4
        
    def save_to_db(self):
        """Save new player to database """
        tournaments_db = TinyDB('data/tournaments.json')
        tournaments_db.all()
        tournament_id = len(tournaments_db.all()) + 1
        tournament_id = tournaments_db.insert({
            "id": tournament_id,
            "name": self.name,
            "location": self.location,
            "starting_date": self.starting_date,
            "ending_date": self.ending_date,
            "rounds_total": self.rounds_total, 
            "rounds": self.rounds,
            "current_round": self.current_round,
            "players": self.players,
            "description": self.description
        })
        print("New tournament: " + self.name +", in "+ self.location + " starting on " + self.starting_date + " successfully saved")

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
    

