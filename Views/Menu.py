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
        print("\n\n====== MAIN MENU ======")
        print("[1] Create new tournament")
        print("[2] Create new player")
        print("[3] Reports")
        print("[4] Quit")
        menu_selection = input('\nType [option] and press ENTER :')
        return menu_selection

    def main_menu_extra(current_tournament, current_round):
        print("\n=== ***** ===\n")
        print("- Tournament : " + current_tournament["name"].upper())
        print("- Current round: " + str(current_round["round_id"]))
        print("Ready to go to the next round ?\n")
        print("\n=== MENU ===\n")
        print("[1] YES")
        print("[2] EXIT")

    def input_prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    def input_prompt():
        print("\nType [option] and press Enter : ", end='')

