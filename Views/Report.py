
class ReportsView:

    def __init__(self):
        pass

    @staticmethod
    def reports_menu():
        print("\n" * 3 + "--- REPORTS ---\n")
        print("[1] All players")
        print("[2] Players in a tournament")
        print("[3] All tournaments")
        print("[4] Rounds in a tournament")
        print("[5] Matches in a tournament")
        print("\n[back] Back to main menu")
    
    @staticmethod
    def reports_player_sorting():
        print("\n[1] Sort by name")
        print("[2] Sort by score")
        print("\n[back] Back to main menu")