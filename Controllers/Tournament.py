
import random
from datetime import date
from time import gmtime, strftime

from Views.Tournament_Menu import MenuTournamentView
from Views.Menu import MenuView
from Models.Tournament import Tournament
from Models.Round import Round

class TournamentController:
    
    def __init__(self):
        pass
    
    def create_tournament(self): 
        ''' Function : create_tournament

            Parameters
            ----------
            no parameters
            ----------
            Return
            ----------
            player: Tournament
                    player information
        '''
        tournament_information = {}
        tournament_attrs = [
            "name",
            "location",
            "description"
        ]

        for item in tournament_attrs:
            MenuView.input_prompt_text(item)
            user_input = input()
            if user_input == "back":
                return None
            else:
                tournament_information[item] = user_input
        
        tournament = Tournament(tournament_information["name"], tournament_information["location"],  str(date.today()), "", tournament_information["description"])
        return tournament
    
    def save_tournament(self, tournament):
        ''' Function : create_player

            Parameters
            ----------
            player: Tournamement
                    tournament information
            
            Return
            ----------
            no return
        '''
        MenuTournamentView.start()
        user_input = input().lower()
        if user_input == "1":
           return tournament
        elif user_input == "2":
           return None
      
 
    def select_randomly(self, players):
        random.shuffle(players)
        return players
    
    def create_round(self, players):
        id_list = []
        players_pairs = []
        today = date.today()
        _round = Round(1, today, "", strftime("%H:%M", gmtime()), players)
        i = 0
        while i < len(players):
            players_pairs.append((players[i], players[i+1]))
            i+=2
        return players_pairs

    def play_rounds(self, players_pairs):
        rounds = Tournament.getRounds_total()
        i = 0
        while i < rounds:
            i+=1
            for player in players_pairs:
                print(i)
                winner = random.randint(0, len(player))
                if winner == 2:
                    player[0]["score"] += 0.5
                    player[1]["score"] += 0.5
                else:
                    player[0]["score"] += 0 if winner == 1 else 1
                    player[1]["score"] += 0 if winner == 0 else 1
         
        return players_pairs
             


    def display_players(self):
        ''' Function : display_players

            Parameters
            ----------
            no parameters
            ----------
            no return
        '''

        players = Player.load_player_db()
        id_list = []
        tour_players = []
        for i in range(len(players)):
            id_list.append(players[i]["id"])
        i = 0
        while i < len(players):
            player = MenuView.display_players(players, i)
            tour_players.append(player)
            i+=1
        return tour_players
