from prettytable import PrettyTable
from Controllers.Database import Database


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
        """Player report (sorted by rank)
        @param players: list of players
        """
        players = sorted(players, key=lambda x: x.get('score'), reverse=True)
        self.display_players(players, "by rank")

