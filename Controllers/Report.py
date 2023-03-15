from prettytable import PrettyTable
from Views.Report import ReportsView
from Models.Round import Round
from Models.Player import Player
from Models.Tournament import Tournament

class ReportsController:

    def __init__(self):
        self.table = PrettyTable()

    def return_tournament_rounds(self, input):
        number_input = int(input)
        tournaments = Tournament.load_tournament_db()
        tournament = tournaments[number_input - 1]
        tournament_id = tournament["tournament_id"]
        rounds = Round.load_round_db()
        tournament_rounds = list(filter(lambda r: r["tournament_id"] == tournament_id, rounds))
        return tournament, tournament_rounds

    def display_players(self, players: list, sorting: str):
        """Print players reports """
        self.table.clear()
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
        tournaments = Tournament.load_tournament_db()
        user_input = ReportsView.reports_tournaments(tournaments)
        if user_input == "back":
            return "back"
        else:
            return int(user_input) - 1

    def display_tournament_report(self, select_input: str):
        """Display all tournaments
            @param select_input: string
        """
        self.table.clear()
        self.table.field_names = [
            "Name",
            "Location",
            "Start Date",
            "End Date",
        ]
        tournaments = Tournament.load_tournament_db()
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
        self.table.clear()
        self.table.field_names = [
            "Round #",
            "Starting Date",
            "Starting Time",
            "Ending Time",
            "Matches"
        ]

        tournament, tournament_rounds = self.return_tournament_rounds(select_input)

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

    def display_tournament_match_report(self, select_input: str):
        """Display all rounds in tournanment to select
        @param select_input: string
        """
        self.table.clear()
        self.table.field_names = [
            "Round #",
            "Player 1",
            "Score P1",
            "",
            "Player 2",
            "Score P2",
        ]

        tournament, _ = self.return_tournament_rounds(select_input)
        rounds = Round.load_round_db()
        print(rounds)
        _round = rounds[-1]
        pairs = _round['pairs']

        self.display_header(tournament, _round)
        for pair in pairs:
            first_1 = pair[0]["last"].capitalize()
            last_1 = pair[0]["first"]
            player_1 = last_1 + ", " + first_1
            score_1 = pair[0]["score"]

            first_2 = pair[1]["last"].capitalize()
            last_2 = pair[1]["first"]
            player_2 = last_2 + ", " + first_2
            score_2 = pair[1]["score"]
            self.table.add_row([
                tournament['current_round'],
                player_1,
                score_1,
                "vs",
                player_2,
                score_2,
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
        self.table.clear()
        self.table.field_names = [
            "Player",
            "Last",
            "First",
            "Dob",
            "Color",
            "Score",
            " "
        ]
        tournament, tournament_rounds = self.return_tournament_rounds(select_input)
        players = tournament["players"]
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
                "---"
            ])
            self.table.add_row([
                "Player 1",
                pair[0]["last"].upper(),
                pair[0]["first"],
                pair[0]["dob"],
                pair[0]["color"],
                pair[0]["score"],
                self.return_winner(pair[0], pair[1])
            ])
            self.table.add_row([
                "Player 2",
                pair[1]["last"].upper(),
                pair[1]["first"],
                pair[1]["dob"],
                pair[1]["color"],
                pair[1]["score"],
                self.return_winner(pair[1], pair[0])
            ])
        print(self.table)

    def display_tournament_intermediate_report(self, tournament_info):
        self.table.clear()
        self.table.field_names = [
            "Round #",
            "Player 1",
            "Score P1",
            "",
            "Player 2",
            "Score P2",
        ]

        rounds = Round.load_round_db()
        _round = rounds[len(rounds) - 1]
        pairs = _round['pairs']

        tournament_info["current_round"] = len(rounds) - 1
        tournament_info["rounds_total"] = 4
        print("\n ==== END round # " + str(len(rounds)) + " ==== \n")
        self.display_header(tournament_info, _round)
        for pair in pairs:
            first_1 = pair[0]["last"].capitalize()
            last_1 = pair[0]["first"]
            player_1 = last_1 + ", " + first_1
            score_1 = pair[0]["score"]

            first_2 = pair[1]["last"].capitalize()
            last_2 = pair[1]["first"]
            player_2 = last_2 + ", " + first_2
            score_2 = pair[1]["score"]
            self.table.add_row([
                tournament_info['current_round'],
                player_1,
                score_1,
                "vs",
                player_2,
                score_2,
            ])
        print(self.table)

    def display_ranking_report(self):
        self.table.clear()
        self.table.field_names = [
            "Player",
            "Score",
            "Rank",
        ]

        players = Player.load_players_db()
        for player in players:
            first = player["last"].capitalize()
            last = player["first"]
            fullName = first + ", " + last
            score = player["score"]

            self.table.add_row([
                fullName,
                score,
                0
            ])
        print(self.table)

    def display_header(self, tournament, round):
        """Header for tournament reports
        @param info: tournament (dict)
        """
        h_1 = f"Tournoi: {tournament['name'].upper()}, Location: {tournament['location']} | Description : {tournament['description']}"
        h_2 = \
            f"Start date : {round['starting_date']} | " \
            f"Round  : {tournament['current_round']}/{tournament['rounds_total']}"
        print(h_1)
        print(h_2)
