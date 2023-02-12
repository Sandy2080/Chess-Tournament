from datetime import date
from time import gmtime, strftime

from Views.Menu import MenuView
from Views.Player_Menu import MenuPlayerView
from Views.Tournament_Menu import MenuTournamentView
from Models.Player import Player
from Models.Round import Round
from Models.Tournament import Tournament

class MenuController:

    def __init__(self):
        self.menu_view = MenuView()
        self.player_menu_view = MenuPlayerView()
    
    def start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        MenuView.main_menu()
        user_input = input().lower()
        print("you selected option: " + user_input)

        if user_input == "1":
            tournament = self.create_tournament()
            if tournament:
               self.save_tournament(tournament)
        elif user_input == "2":
            player = self.create_player()
            if player:
               self.save_player(player)
        elif user_input == "3":
            self.create_reports()
        else:
            self.start()

    
        

    def start_tournament(self,info, players):
        ''' Function : start_tournament

            Parameters
            ----------
            info : string
                   tournament info
            Returns
            ----------
            players : list
                      list of player in tour
        '''
        pairs = self.create_round(players)
        print(pairs)
        print("\n\nNew tournament created :\n")
        for key, value in info.items():
            print(f"- {key}: {value}", end='\n')
        print("- Players " + str(len(players)) +"\n")
        print("- current round : 1")
        tournament = Tournament(info["name"],info["location"], date.today(), "", 10, players, pairs,  0, "")
        tournament.describe()

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

    def _create_tournament(self):
        """Create new tournament"""
        players = self.display_players()
        self.start_tournament(tournament_information, players)

    def create_reports(self):
        print("creating reports")