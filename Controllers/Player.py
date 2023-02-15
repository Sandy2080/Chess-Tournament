
from datetime import date

from Views.Menu import MenuView
from Views.Player import MenuPlayerView
from Models.Player import Player

class PlayerController:
    
    def __init__(self):
        pass

    def create_player(self): 
        ''' Function : create_player

            Parameters
            ----------
            no parameters
            ----------
            Return
            ----------
            player: Player
                    player information
        '''
        player_information = {}
        player_attrs = [
            "first", 
            "last", 
            "dob"
        ]
        
        for attr in player_attrs:
            print("What is " + attr + "?")
            user_input = input().lower()
            if user_input == "back":
                self.start()
            else:
                player_information[attr] = user_input
        player = Player(player_information["first"], player_information["last"], player_information["dob"], 0)
        return player
       
    def save_player(self, player):
        ''' Function : save_player

            Parameters
            ----------
            player: Player
                    player information
            ----------
            no return
        '''
        MenuPlayerView.start()
        user_input = input().lower()
        if user_input == "1":
            player.save_to_db()
        else:
            self.start()
        str(player)
    

    def display_players(self):
        ''' Function : display_players

            Parameters
            ----------
            no parameters
            ----------
            player: list
                    players
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