from datetime import date
from time import gmtime, strftime

from Models.Tournament import Tournament
from Models.Player import Player
from Models.Round import Round
from Views.Menu import MenuView
from Views.Player import MenuPlayerView
from Views.Tournament import MenuTournamentView
from Controllers.Tournament import TournamentController
from Controllers.Player import PlayerController
 
class Controller:
 
    def __init__(self):
        self.menu_view = MenuView()
        self.player_menu_view = MenuPlayerView()
        self.tournamentView = MenuTournamentView()
        self.tournamentController = TournamentController()
        self.playerController = PlayerController()
    
    def start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        option = MenuView.main_menu()
        user_input = option.lower()
        if user_input == "1":
            # ask for tournament information
            self.create_tournament()
            # ask for confirmation and save
        elif user_input == "2":
            player = self.playerController.create_player()
            if player:
               self.playerController.save_player(player)
        elif user_input == "3":
            self.create_reports()
        else:
            self.start()  

    def restart(self, tournament):
        """Main menu selector :
        Redirects to respective submenus"""

        MenuView.main_menu_extra(tournament.name)
        user_input = input().lower()
        if user_input == "1":
            self.resume_tournament()
        elif user_input == "2":
            self.create_tournament()
        elif user_input == "3":
            self.create_player()
        elif user_input == "4":
            self.create_reports()
        else:
            self.start()   

    def create_tournament(self):
        """Create new tournament"""
        players = Player.load_player_db()
        tournament_informations = self.tournamentView.ask_tournament_info() 
        tournament = self.tournamentController.create_tournament(tournament_informations)
       
        if tournament is None:
            self.start()
        else:
            players = self.tournamentController.select_randomly(players)
            (_round, players_pairs) = self.tournamentController.create_round(players)
            tournament = self.tournamentController.play_round(players_pairs)
            self.tournamentController.save_tournament(tournament)
            tournament.insert_to_db()
            _round.insert_to_db(tournament)
            self.restart(tournament)   
            #tournament = self.tournamentController.save_tournament(tournament)
     
    def resume_tournament(self):
        tournaments = Tournament.load_tournament_db()
        rounds = Round.load_round_db()
        current_round = len(rounds) + 1
        today = date.today()
        tournament = tournaments[-1]
        tournament = self.tournamentController.play_round(tournament["players"])
        _round = Round(current_round, str(today), "", str(strftime("%H:%M", gmtime())), "", tournament.players)
        _round.insert_to_db(tournament)

    def create_player(self):
        player = self.playerController.create_player()
        if player is not None:
            self.playerController.save_player(player)

    def create_reports(self):
        print("creating reports")