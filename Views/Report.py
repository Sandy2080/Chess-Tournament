
class ReportsView:

    def __init__(self):
        pass

    @staticmethod
    def reports_menu():
        print("\n--- REPORTS ---\n")
        print("[1] All players")
        print("[2] All tournaments")
        print("[3] Players in a tournament")
        print("[4] Rounds in a tournament")
        print("\n[back] Back to main menu")
        print("\nType [option] and press ENTER")

    @staticmethod
    def reports_round_menu():
        print("\n--- REPORTS ---\n")
        print("select round number: ")

    @staticmethod
    def reports_player_sorting():
        print("\n[1] Sort by name")
        print("[2] Sort by score")
        print("[back] Back to main menu")

    @staticmethod
    def reports_tournaments(tournaments: dict) -> str:
        """Display all tournaments to select
        @param tournaments: tournaments list
        """

        if len(tournaments) <= 0:
            print("No tournaments to select")
            print("Press [back] to go back to main menu")
        else:
            print("\n--- SELECT TOURNAMENT ---\n")
            for i in range(len(tournaments)):
                print(f"[{i+1}]", end=' ')
                print(tournaments[i]['name'], end=' | ')
                print(tournaments[i]['location'], end=" | ")
                print(f"Start : {tournaments[i]['starting_date']}", end=' | ')
                print(f"End: {tournaments[i]['ending_date']}", end=' | ')
                print(f"Round {tournaments[i]['current_round']-1}/{tournaments[i]['rounds_total']}")
            print("\nSelect Tournament :")
        return input()
