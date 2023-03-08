from prettytable import PrettyTable
from Models.Database import Database
from Views.Report import ReportsView


class ReportsController:

    def __init__(self):
        self.db = Database()
        self.table = PrettyTable()
  
    def display_players(self, players: list, sorting: str):
        """Print players reports """
        self.table = PrettyTable()
        self.table.field_names = [
            "id",
            "last",
            "first",
            "dob",
            "score",
        ]
        self.table.align = "l"
        for i in range(len(players)):
            self.table.add_row([
                players[i]["id"],
                players[i]["last"],
                players[i]["first"],
                players[i]["dob"],
                players[i]["score"]
            ])
        print(f"\n\n\n- All players ({sorting}) -\n")
        print(self.table)

    def all_players_by_name(self, players: list):
        """Print player report (sorted by last name)
        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('last'))
        self.display_players(players, "by name")

    def all_players_by_score(self, players: list):
        """Print player report (sorted by score)
        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('score'), reverse=True)
        self.display_players(players, "by score")
    
    def tournament_select(self):
        """Load all tournaments for selection
        @return: user selection, list of all tournaments
        """
        tournaments = self.db.load_tournament_db()
        user_input = ReportsView.reports_tournaments(tournaments)
        if user_input == "back":
            return "back"
        else:
            return int(user_input) - 1
    
    def display_tournament_report(self, select_input: str):
        """Display all tournaments
            @param select_input: string
        """  
        self.table = PrettyTable() 
        self.table.field_names = [
            "Name",
            "Location",
            "Start Date",
            "End Date",
        ]
        tournaments = self.db.load_tournament_db()
        tournament = tournaments[select_input - 1]

        print("you selected tournament #: " + str(select_input + 1))
        self.table.add_row([
            tournament['name'],
            tournament['location'],
            tournament['starting_date'],
            tournament['ending_date']
        ])
        print(self.table)
            
    def display_tournament_report_rounds(self, select_input: str):
        """Display all rounds in tournanment to select
        @param select_input: string
        """
        self.table = PrettyTable()
        self.table.field_names = [
            "Round #",
            "Starting Date",
            "Starting Time",
            "Ending Time",
            "Matches"
        ]
  
        tournaments = self.db.load_tournament_db()
        tournament = tournaments[select_input - 1]
        tournament_id = tournament["tournament_id"]
        rounds = self.db.load_round_db()
        tournament_rounds = list(filter(lambda r: r["tournament_id"] == tournament_id, rounds))
       
        print("\n ====================\n Tournament: " + str(tournament['name']) + "\n ==================== \n")
        print(" -number of rounds :" + str(len(tournament_rounds)))
        
        for _round in tournament_rounds:
            self.table.add_row([
                _round['round_id'],
                _round['starting_date'],
                _round['starting_time'],
                _round['ending_time'],
                str(len(_round['pairs'])),
            ])
        print(self.table)
    
    def return_winner(self, pair1, pair2):
        if pair1["score"] > pair2["score"]:
            return "WINNER"
        elif pair1["score"] == pair2["score"]:
            return "NULL"
        else:
            return ""
    
    def display_tournament_report_players(self, select_input: str):
        """Display all tournaments to select
        @param tournaments: tournaments list
        """
        i = 0
        self.table = PrettyTable()
        self.table.field_names = [
            "Player",
            "First",
            "Last",
            "Dob",
            "Genre",
            "Color",
            "Score", 
            ""
        ]

        tournaments = self.db.load_tournament_db()
        tournament = tournaments[select_input - 1]
        players = tournament["players"]
        tournament_id = tournament["tournament_id"]
        rounds = self.db.load_round_db()
        tournament_rounds = list(filter(lambda r: r["tournament_id"] == tournament_id, rounds))
       
        print("\n ====================\n Tournament: " + str(tournament['name']) + " / location : " + tournament['location'] + "\n ==================== \n")
        print(" -number of rounds :" + str(len(tournament_rounds)))
       
        i = 0
        for pair in players:
            i = i + 1
            self.table.add_row([
                "Pair: " + str(i),
                "---",
                "---",
                "---",
                "---",
                "---",
                "---",
                "---"
            ])

            self.table.add_row([
                "Player 1",
                pair[0]["last"].upper(),
                pair[0]["first"],
                pair[0]["dob"],
                pair[0]["genre"],
                pair[0]["color"],
                pair[0]["score"], 
                self.return_winner(pair[0], pair[1])
            ])
            self.table.add_row([
                "Player 2",
                pair[1]["last"].upper(),
                pair[1]["first"],
                pair[1]["dob"],
                pair[1]["genre"],
                pair[1]["color"],
                pair[1]["score"],
                self.return_winner(pair[1], pair[0])
            ])
        print(self.table)
          
       
