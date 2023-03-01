
class ReportsView:

    def __init__(self):
        pass

    @staticmethod
    def reports_menu():
        print("\n" * 3 + "--- REPORTS ---\n")
        print("[1] All players")
        print("[2] All tournaments")
        print("[3] Players in a tournament")
        print("[4] Rounds in a tournament")
        print("[back] Back to main menu")
    
    @staticmethod
    def reports_player_sorting():
        print("\n[1] Sort by name")
        print("[2] Sort by score")
        print("[back] Back to main menu")
    
    @staticmethod
    def reports_tournaments(tournaments):
        """Display all tournaments to select
        @param tournaments: tournaments list
        """
        print("\n" * 2 + "--- SELECT TOURNAMENT ---\n")

        for i in range(len(tournaments)):
            print(f"[{tournaments[i]['tournament_id']}]", end=' ')
            print(tournaments[i]['name'], end=' | ')
            print(tournaments[i]['location'], end=" | ")
            print(tournaments[i]['description'], end=' | ')
            print(f"Started on : {tournaments[i]['starting_date']}", end=' | ')
            print(f"Ended on : {tournaments[i]['ending_date']}", end=' | ')
            print(f"Round {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}")
        print("\n\n Select Tournament :")  
        return input()

