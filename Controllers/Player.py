import random
from Controllers.utilities import input_text_field
from Views.Menu import MenuView
from Views.Player import MenuPlayerView
from Models.Player import Player

class PlayerController:

    def __init__(self):
        pass

    def ask_player_info(self) -> dict:
        player_informations = {}
        player_attrs = [
            "first",
            "last",
            "dob"
        ]

        for item in player_attrs:
            user_input = input().lower()
            if user_input == "back":
                self.start()
            player_informations[item.lower()] = input_text_field(item)
        return player_informations

    def select_randomly(self, players: list) -> list:
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

    def create_player(self, player_information: dict) -> Player:
        ''' Function : create_player

            Parameters
            ----------
            player_information: dict
            ----------
            Return
            ----------
            player: Player
                    player information
        '''

        player = Player(player_information["first"], player_information["last"], player_information["dob"], 0)
        return player

    def save_player(self, player: Player):
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
            i += 1
        return tour_players