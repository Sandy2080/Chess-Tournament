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
from Controllers.Database import Database
 
class Controller:
 
    def __init__(self):
        self.menu_view = MenuView()
        self.player_view = MenuPlayerView()
        self.tournamentView = MenuTournamentView()
        self.tournamentController = TournamentController()
        self.playerController = PlayerController()
        self.tournament = Tournament()
        self.db = Database()
    
    def start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        option = MenuView.main_menu()
        user_input = option.lower()
        if user_input == "1":
            self.create_tournament()
        elif user_input == "2":
            self.create_player()
        elif user_input == "3":
            self.create_reports()
        else:
            self.start()  

    def continueGame(self): 
        rounds = self.db.load_round_db()
        current_round = rounds[-1]
        round_id = current_round["round_id"]
        tournaments = self.db.load_tournament_db()
        current_tournament = tournaments[-1]
        if round_id <= 4:
            self.resume_tournament(current_tournament, current_round)
        else:
            self.start()

    def create_tournament(self):
        """Create new tournament"""
        players = self.db.load_players_db()
        tournament_informations = self.tournamentController.ask_tournament_info() 
        tournament = self.tournamentController.create_tournament(tournament_informations)
        
        if tournament is not None:
            players = self.tournamentController.select_randomly(players)
            (_round, players_pairs) = self.tournamentController.create_round_and_select_players((players))
            players = self.tournamentController.black_or_white(players_pairs)
            tournament = self.tournamentController.play_round(players)
            tournament = self.tournamentController.save_tournament(tournament_informations, players_pairs)
            self.continueGame()   
        else:
            self.start()    
            
    def resume_tournament(self, tournament, round):
        MenuView.main_menu_extra(tournament, round)
        user_input = input().lower()
        if user_input == "1":
            self.start_next_round()
        elif user_input == "2":
            self.create_tournament()
        elif user_input == "3":
            self.create_player()
        elif user_input == "4":
            self.create_reports()
        else:
            self.start()   

    def start_next_round(self):
        all_players = self.db.load_players_db()
        tournaments = self.db.load_tournament_db()
        current_tournament = tournaments[-1]
        (_round, players_pairs) = self.tournamentController.create_round_and_select_players(all_players)
        players = self.tournamentController.black_or_white(players_pairs)
        self.tournamentController.play_round(players)
        self.tournamentController.save_tournament(current_tournament, players_pairs)
        self.continueGame()  
 
    def create_player(self):
        player_informations = self.playerController.ask_player_info()
        player = self.playerController.create_player(player_informations)
    
        if player is not None:
            self.playerController.insert_player_to_db(player)
            self.start()
        else:
            print("player is none")

    def create_reports(self):
        print("creating reports")