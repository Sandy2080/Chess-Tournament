from datetime import date

from Views.Menu import MenuView
from Controllers.utilities import input_text_field, date_text_field

class MenuTournamentView:

    def __init__(self):
        pass 

    def ask_tournament_info(self) -> dict:
        """Ask to user to type the tournament informations

        Returns:
            dict: tournament informations
        """

        tournament_information = {}
        tournament_attrs = [
            "Name",
            "Location",
            "description"
        ]
        for item in tournament_attrs:
            tournament_information[item.lower()] = input_text_field(item)

        start_date = date_text_field('starting date (jj/mm/aaaa): (if empty, starting date is today) ')
        end_date = date_text_field("ending date (jj/mm/aaaa) : : (if empty, ending date is in one day) ' ")

        tournament_information['start_date'] = start_date
        tournament_information['end_date'] = end_date 
        print(tournament_information)
        return tournament_information

    def start():
        print("\n\n=== Create Tournament ? ===\n")
        print("[1] save")
        print("[2] cancel")

   
