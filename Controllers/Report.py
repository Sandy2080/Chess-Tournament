from prettytable import PrettyTable
from Models.Database import Database
from Views.Report import ReportsView


class ReportsController:

    def __init__(self):
        self.db = Database()
        self.table = PrettyTable()

        self.player_report_field_names = [
            "id",
            "last",
            "first",
            "dob",
            "score",
        ]
  
    def display_players(self, players, sorting):
        """Display player report (all sorting types)"""
        self.table.field_names = self.player_report_field_names
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

    def all_players_by_name(self, players):
        """Player report (sorted by last name)
        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('last'))
        self.display_players(players, "by name")

    def all_players_by_score(self, players):
        """Player report (sorted by score)
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
    
    def display_tournament_report(self, select_input):
        """Display all tournaments
            @param select_input: string
        """
         
        tournaments = self.db.load_tournament_db()
        tournament = tournaments[select_input - 1]
        print("****" + tournament['name'] + "****")
        print("-location: " + tournament['location'])
        print("-description:" + tournament['description'])
        print("- Started on :" + tournament['starting_date'])
        print("- Ended on :" + tournament['starting_date'])
        self.table.add_row([
                tournament['name'],
                tournament['location'],
                tournament['description'],
                tournament['starting_date'],
                tournament['ending_date']
            ])
            
    def display_tournament_report_rounds(self, select_input):
        """Display all rounds in tournanment to select
        @param select_input: string
        """
        self.table.field_names = [
            "Round #",
            "Starting Date",
            "Ending Date",
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
        print(" -number of rounds :" + tournament["name"] + ": " + str(len(tournament_rounds)))
        
        for _round in tournament_rounds:
            self.table.add_row([
                _round['round_id'],
                _round['starting_date'],
                _round['ending_date'],
                _round['starting_time'],
                _round['ending_time'],
                str(len(_round['pairs'])),
            ])
        print(self.table)
    
    def display_tournament_report_players(self, select_input):
        """Display all tournaments to select
        @param tournaments: tournaments list
        """
        i = 0
        tournaments = self.db.load_tournament_db()
        tournament = tournaments[select_input - 1]
        players = tournament["players"]

        print("****" + tournament['name'] + "****")
        print("-" + tournament['location'])
        for pair in players:
            i += 1
            print(str(i)+"/ player 1: " + pair[0]["last"].upper() + ", " + pair[0]["first"])
            print("  - score: " + str(pair[0]["score"]))
            i += 1
            print(str(i)+"/ player 2: " + pair[1]["last"].upper() + ", " + pair[1]["first"])
            print("  - score: " + str(pair[1]["score"]))
            print("------")