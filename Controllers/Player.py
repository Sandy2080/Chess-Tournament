
from datetime import date

from Views.Menu import MenuView
from Views.Player_Menu import MenuPlayerView
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
        ''' Function : create_player

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