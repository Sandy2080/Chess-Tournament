from datetime import date
from time import gmtime, strftime

from Models.Player import Player
from Models.Round import Round
from Views.Menu import MenuView
from Views.Player_Menu import MenuPlayerView
from Controllers.Tournament import TournamentController
from Controllers.Player import PlayerController
 
class MenuController:
 
    def __init__(self):
        self.menu_view = MenuView()
        self.player_menu_view = MenuPlayerView()
        self.tournamentController = TournamentController()
        self.playerController = PlayerController()
    
    def start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        MenuView.main_menu()
        user_input = input().lower()
        print("you selected option: " + user_input)

        if user_input == "1":
            tournament = self.tournamentController.create_tournament()
            players = Player.load_player_db()
            players = self.tournamentController.select_randomly(players)
            players_pairs = self.tournamentController.create_round(players)
            print(players)
            if tournament:
               self.tournamentController.save_tournament(tournament)

        elif user_input == "2":
            player = self.playerController.create_player()
            if player:
               self.playerController.save_player(player)

        elif user_input == "3":
            self.create_reports()
        else:
            self.start()   


    def _create_tournament(self):
        """Create new tournament"""
        players = self.display_players()
        self.tournament.start_tournament(tournament_information, players)

    def create_reports(self):
        print("creating reports")