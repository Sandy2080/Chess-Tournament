
import random
from tinydb import TinyDB
from datetime import date
from time import gmtime, strftime
from Controllers.utilities import input_text_field, date_text_field, SCORE_LOOSER, SCORE_WINNER, SCORE_NULL 

from Controllers.Database import Database
from Views.Tournament import MenuTournamentView
from Models.Tournament import Tournament
from Models.Round import Round
class TournamentController:
 
    def __init__(self):
        self.tournament = Tournament()
        self.db = Database()

    def create_tournament(self, tournament_information): 
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
       
        # self.tournament.toJSON(tournament_information)
        return self.tournament
    
    def save_tournament(self, tournament, pairs):
        ''' Function : save_tournament

            Parameters
            ----------
            tournament: Tournament
                        tournament information
            
            Return
            ----------
            no return
        '''
        MenuTournamentView.start()
        user_input = input().lower()
        players = []
        if user_input == "1":
            tournament_id = self.db.save_tournament_to_db(tournament, pairs)
            round_id = self.db.save_round_to_db(tournament_id, pairs)
            self.db.update_tournament_db(tournament_id, round_id)
            
            # update scores
            for pair in pairs:
                [player_1, player_2] = pair
                self.db.update_player_score(player_1)
                self.db.update_player_score(player_2)
                players.append(player_1)
                players.append(player_2)

            # sort players by score
            self.sort_players_and_save_to_db(players)
            return tournament
        elif user_input == "2":
            return None

    def update_tournament(self, tournament, round_id):
        _tournament = tournament[-1]
        self.db.update_tournament_db(_tournament["id"], round_id)
        return tournament

    def ask_tournament_info(self) -> dict:
        """Ask to user to type the tournament informations

        Returns:
            dict: tournament informations
        """

        tournament_information = {}
        tournament_attrs = [
            "Name",
            "Location",
            "description"
        ]
        for item in tournament_attrs:
            tournament_information[item.lower()] = input_text_field(item)

        start_date = date_text_field('starting date (jj/mm/aaaa): (if empty, starting date is today) ')
        end_date = date_text_field("ending date (jj/mm/aaaa) : : (if empty, ending date is in one day) ' ")

        tournament_information['starting_date'] = start_date
        tournament_information['ending_date'] = end_date
        return tournament_information

    def select_randomly(self, players):
        ''' Function : select_randomly
            Parameters
            ----------
            players: list
                     list of players
            ----------
            Return
            ----------
            players: list
                     list of players
        '''
        random.shuffle(players)
        return players
    
    def black_or_white(self, players_pairs):
        colors = ["black", "white"]
        for player in players_pairs:
            rand = random.randrange(len(player))
            player[0]["color"] = colors[rand]
            player[1]["color"] = "white" if colors[rand] == "black" else "black"
        return players_pairs
    
    def play_round(self, players_pairs):
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

    def create_round_and_select_players(self, players):
        players_pairs = []
        today = date.today()
        rounds = self.db.load_round_db()
        current_round = len(rounds) + 1
        _round = Round(current_round, str(today), "", str(strftime("%H:%M", gmtime())), "", players)
        i = 0
        while i < len(players) - 1:
            players_pairs.append((players[i], players[i+1]))
            i += 2
        self.tournament.players = players_pairs
        return (_round, players_pairs)
    
    def sort_players_and_save_to_db(self, players):
        score_sorted_players = sorted(players, key=lambda x: x["score"], reverse=True)
        
        players = self.db.remove_records(score_sorted_players)
   
        for player in score_sorted_players:
            self.db.insert_player_to_db(player)

        # today = date.today()      
        # _round = Round(current_round, str(today), "", str(strftime("%H:%M", gmtime())), "", players)
        # return (_round, score_sorted_players)

    

