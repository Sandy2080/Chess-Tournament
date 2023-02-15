
import random
from datetime import date
from time import gmtime, strftime

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
    
    def save_tournament(self, tournament):
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
           return tournament
        elif user_input == "2":
           return None
      
 
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
    
    def create_round(self, players):
        id_list = []
        players_pairs = []
        today = date.today()
        _round = Round(1, str(today), "", str(strftime("%H:%M", gmtime())), "", players)
        i = 0
        while i < len(players):
            players_pairs.append((players[i], players[i+1]))
            i+=2
        self.tournament.players = players_pairs
        return (_round, players_pairs)

    def play_round(self, players_pairs):
        rounds = self.tournament.getRounds_total()
        for player in players_pairs:
            winner = random.randint(0, len(player))
            if winner == 2:
                player[0]["score"] += 0.5
                player[1]["score"] += 0.5
            else:
                player[0]["score"] += 0 if winner == 1 else 1
                player[1]["score"] += 0 if winner == 0 else 1   
        self.tournament.players = players_pairs 
        self.tournament.increment_round()
        return self.tournament

    def black_or_white(self, players_pairs):
        colors = ["black", "white"]
        for player in players_pairs:
            rand = random.randrange(len(player))
            player[0]["color"] =  colors[rand]
            player[1]["color"] =  "white" if colors[rand] == "black" else "black"

    def sort():
        pass

