import random
from datetime import date, timedelta
from time import gmtime, strftime

from Views.Tournament import MenuTournamentView
from Models.Tournament import Tournament
from Models.Player import Player
from Models.Round import Round

from Controllers.utilities import input_text_field, SCORE_LOOSER, SCORE_WINNER, SCORE_NULL

class TournamentController:

    def __init__(self):
        self.tournament = Tournament()

    def create_tournament(self, tournament_information: dict) -> Tournament:
        ''' Function : create_tournament

            Parameters
            ----------
            tournament_information: dict

            ----------
            Return
            ----------
            player: Tournament
                    player information
        '''

        self.tournament.toObject(tournament_information)
        return self.tournament

    def save_tournament(self, tournament, pairs):
        ''' Function : save_tournament

            Parameters
            ----------
            tournament: Tournament
                        tournament information

            Return
            ----------
            Tournament or None
        '''
        MenuTournamentView.start()
        user_input = input().lower()
        players = []
        if user_input == "1":
            # interroger bd pour current tournament
            tournament_id = self.tournament.save_tournament_to_db(tournament, pairs)
            round_id = self.tournament.save_round_to_db(tournament_id, pairs)
            Tournament.update_tournament_db(tournament_id, round_id)

            # update scores
            for pair in pairs:
                [player_1, player_2] = pair
                Player.update_player_score(player_1)
                Player.update_player_score(player_2)
                players.append(player_1)
                players.append(player_2)

            # sort players by score
            self.sort_players_and_save_to_db(players)
            return tournament
        elif user_input == "2":
            return None

    def update_tournament(self, tournament, round_id):
        _tournament = tournament[-1]
        Tournament.update_tournament_db(_tournament["tournament_id"], round_id)
        return tournament

    def ask_tournament_info(self) -> dict:
        ''' Function : ask_tournament_info
            Ask for the tournament informations

            Parameters
            ----------
            tournament: Tournament
                        tournament information

            Return
            ----------
            dict: tournament informations
        '''
        tournaments = Tournament.load_tournament_db()
        _id = len(tournaments) + 1
        tournament_information = {}
        tournament_attrs = [
            "Name",
            "Location",
            "description"
        ]
        for item in tournament_attrs:
            tournament_information[item.lower()] = input_text_field(item)

        start_date = input_text_field('starting date (jj/mm/aaaa): \n(if empty, starting date is today) ')
        end_date = input_text_field("ending date (jj/mm/aaaa) : \n(if empty, ending date is in one day) ' ")
        tournament_information['tournament_id'] = _id
        tournament_information['starting_date'] = str(date.today()) if start_date == "" else start_date
        tournament_information['ending_date'] = str(date.today() + timedelta(days=1)) if end_date == "" else end_date
        return tournament_information

    def black_or_white(self, players_pairs: dict) -> dict:
        ''' Function : black_or_white
            Player black or white color

            Parameters
            ----------
            dict: player_pairs

            Return
            ----------
            dict: player_pairs
        '''
        colors = ["black", "white"]
        for player in players_pairs:
            rand = random.randrange(len(player))
            player[0]["color"] = colors[rand]
            player[1]["color"] = "white" if colors[rand] == "black" else "black"
        return players_pairs

    def play_match(self, players_pairs: dict) -> dict:
        ''' Function : play_match
            Play a chess match

            Parameters
            ----------
            dict: player_pairs

            Return
            ----------
            dict: tournament
        '''
        for player in players_pairs:
            winner = random.randint(0, len(player))
            if winner == 2:
                player[0]["score"] += SCORE_NULL
                player[1]["score"] += SCORE_NULL
            else:
                player[0]["score"] += SCORE_LOOSER if winner == 1 else SCORE_WINNER
                player[1]["score"] += SCORE_LOOSER if winner == 0 else SCORE_WINNER
        self.tournament.players = players_pairs
        tournament = self.tournament.serialize()
        return tournament

    def select_players(self, players: list) -> list:
        ''' Function : select_players
            Match players randomly and play first round

            Parameters
            ----------
            dict: players

            Return
            ----------
            dict: players_pairs
        '''
        players_pairs = []
        i = 0
        while i < len(players) - 1:
            players_pairs.append((players[i], players[i+1]))
            i += 2
        self.tournament.players = players_pairs
        return players_pairs

    def sort_players_and_save_to_db(self, players: list):
        ''' Function : sort_players_and_save_to_db
            Sort players in ascending order and save list to database

            Parameters
            ----------
            dict: players

            Return
            ----------
            no return
        '''
        score_sorted_players = sorted(players, key=lambda x: x["score"], reverse=True)

        players = Player.remove_records(score_sorted_players)

        for player in score_sorted_players:
            Player.insert_player_to_db(player)



