from Models.Player import Player
from Models.Tournament import Tournament
from datetime import date
from time import gmtime, strftime

def create_player(): 
    player = Player("Sandy", "L", "DD/MM/YY", 0)
    player.save_to_db()
    print(player)

def create_tournament(): 
    tournament = Tournament("Le tournoi", "Paris",  str(date.today()), "", "")
    tournament.save_to_db()
    tournament.describe()

def main():
    pass
    
if __name__ == "__main__":
    main()