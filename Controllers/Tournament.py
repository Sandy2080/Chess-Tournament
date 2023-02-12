
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
                self.start()
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
            ----------
            no return
        '''
        MenuTournamentView.start()
        user_input = input().lower()
        if user_input == "1":
           tournament.save_to_db()
        else:
            self.start()
    
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
            players_pairs.append(({"id": players[i]["id"], "name":players[i]["last"]}, {"id": players[i+1]["id"], "name":players[i+1]["last"]}))
            i+=2
        _round.make_pairs(players_pairs)
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
