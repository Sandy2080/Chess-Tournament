class MenuView:

    def __init__(self):
        pass
        
    def input_text_field(self, user_input):
        if user_input == "back":
            return None
        return input(user_input.lower())

    def main_menu():
        """Main menu.

        Returns:
            menu_value (str): user choice
        """
        print("\n\n----- MAIN MENU -----")
        print("[1] Create new tournament")
        print("[2] Create new player")
        print("[3] Reports")
        print("[4] Quit")
        menu_selection = input('enter menu option :')
        return menu_selection
    
    def main_menu_extra(current_tournament, current_round):
        print("\n=== MAIN MENU ===\n")
        print("*** Tournament : " + current_tournament["name"].upper() + " ***")
        print("current round: " + str(current_round["round_id"]))
        print("ready to go to the next round ?\n")
        print("[1] Resume tournament '" + current_tournament["name"].upper()+"'")
        print("[2] Create new tournament")
        print("[3] Create new player")
        print("[4] Reports")

    def input_prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    def input_prompt():
        print("\nType [option] and press Enter : ", end='')
    
    