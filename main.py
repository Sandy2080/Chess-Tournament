from Views.Menu import MenuView
from Controllers.Menu import MenuController

from Models.Player import Player
from Models.Tournament import Tournament
from datetime import date
from time import gmtime, strftime



def create_tournament(): 
    tournament = Tournament("Le tournoi", "Paris",  str(date.today()), "", "")
    tournament.save_to_db()
    tournament.describe()

def main():
    # MenuView.start()
    MenuController().start()

if __name__ == "__main__":
    main()