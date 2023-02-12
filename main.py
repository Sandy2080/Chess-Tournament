from Views.Menu import MenuView
from Controllers.Menu import MenuController

from Models.Player import Player
from Models.Tournament import Tournament
from datetime import date
from time import gmtime, strftime

def main():
    MenuController().start()

if __name__ == "__main__":
    main()