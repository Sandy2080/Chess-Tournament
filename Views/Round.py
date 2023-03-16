class RoundView:

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
        print("[1] Go to next round")
        print("[2] Start new tournament")
        print("[4] Quit")
        menu_selection = input('enter menu option :')
        return menu_selection
