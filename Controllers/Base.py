from Models.Tournament import Tournament
from Views.Menu import MenuView
from Views.Player import MenuPlayerView
from Views.Tournament import MenuTournamentView
from Controllers.Tournament import TournamentController
from Controllers.Player import PlayerController
from Controllers.Database import Database
 

class BaseController:
 
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
            players = self.playerController.select_randomly(players)
            players_pairs = self.tournamentController.create_round_and_select_players((players))
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
            self.start()
        else:
            self.start()   
    
    def load_pairs(self):
        i = 0
        pairs = self.db.load_pairs()
        players_solo = []
        for pair in pairs:
            players_solo.append(pair[1])
   
        for player in players_solo:
            i += 1
            if i > len(players_solo) - 1:
                i = 0
                pairs[i][1] = player  
            else:  
                pairs[i][1] = player  
            
        return pairs

    def start_next_round(self):
        all_players = self.load_pairs()
        tournaments = self.db.load_tournament_db()
        current_tournament = tournaments[-1]
        players_pairs = self.tournamentController.black_or_white(all_players)
        self.tournamentController.play_round(players_pairs)
        # change to update tournament
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