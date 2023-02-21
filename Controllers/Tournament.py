
import random
from tinydb import TinyDB
from datetime import date
from time import gmtime, strftime
from Controllers.utilities import input_text_field, date_text_field, SCORE_LOOSER, SCORE_WINNER, SCORE_NULL 


from Views.Tournament import MenuTournamentView
from Views.Menu import MenuView
from Models.Tournament import Tournament
from Models.Round import Round

class TournamentController:
    
    def __init__(self):
        self.tournament = Tournament()

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
       
        self.tournament.create(tournament_information["name"], tournament_information["location"],  str(date.today()), "", tournament_information["description"])
        return self.tournament
    
    def save_tournament(self, tournament, _round):
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
        if user_input == "1":
            tournament_id = tournament.insert_to_db()
            round_id = _round.insert_to_db(tournament)
            tournament.update_db(tournament_id, round_id)
            return tournament
        elif user_input == "2":
            return None

    def update_tournament(self, tournament, round_id):
        tournament.update_db(tournament.tournament_id, round_id)

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

        tournament_information['start_date'] = start_date
        tournament_information['end_date'] = end_date 
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
            player[0]["color"] =  colors[rand]
            player[1]["color"] =  "white" if colors[rand] == "black" else "black"
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
        # self§.tournament.increment_round()
        return self.tournament

    def create_round_and_select_players(self, players):
        players_pairs = []
        today = date.today()
        _round = Round(1, str(today), "", str(strftime("%H:%M", gmtime())), "", players)
        i = 0
        while i < len(players) - 1:
            players_pairs.append((players[i], players[i+1]))
            i += 2
        self.tournament.players = players_pairs
        return (_round, players_pairs)
    
    def create_round_and_sort_players(self, players, current_round):
        players_pairs = []
        today = date.today()
        _round = Round(current_round, str(today), "", str(strftime("%H:%M", gmtime())), "", players)  
        return (_round, players_pairs)

    # move to utilities
    def sort_list_by_score(self, players_list_with_score):
        """Sort players by score and by ranking.

        Args:
            players_list_with_score (List): list of players with score:
                [[player, score], [player, score], ...]

        Returns:
            List: sorted_list_by_score, if multiple players have the same score,
                    they are sorted by ranking
        """
        
        sorted_list_by_score = sorted(sorted_list_by_ranking, key=lambda x: x[1], reverse=True)
        return sorted_list_by_score  

    
    

