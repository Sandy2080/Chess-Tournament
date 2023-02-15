from Views.Menu import MenuView
from Controllers.Base import Controller

from Models.Player import Player
from Models.Tournament import Tournament
from datetime import date
from time import gmtime, strftime

def main():
    Controller().start()

if __name__ == "__main__":
    main()