class Tournament:
    """Tournoi d'échec."""

    def __init__(self, name, location, starting_date, ending_date, rounds_total, players, current_round, description, rounds=4):
        """Initialise les modalités du tournoi"""
        self.name = name
        self.location = location
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.rounds_total = rounds_total
        self.current_round = current_round
        self.players = []
        self.description = description
        self.rounds = rounds

    def describe(self):
        print("\n\n----------------------------------")
        print("***Tournament started :" + self.name.upper() + "***")
        print("-Date: "+ str(self.starting_date))
        print("-Location : "+ self.location)
        print("-Rounds : "+ str(self.rounds))
        print("-Current round : "+ str(self.current_round))
        print("-Number of players : "+ str(len(self.players)))


