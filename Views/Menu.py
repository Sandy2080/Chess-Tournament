from utilities import bcolors


blue = bcolors["blue"]
cyan = bcolors["cyan"]
green = bcolors["green"]
header = bcolors["header"]
white = bcolors["white"]
yellow = bcolors["yellow"]


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
        print(white + "\n\n====== MAIN MENU ======" + white)
        print(green + "[1] ♟️ Create new tournament" + green)
        print(yellow + "[2] Create new player" + yellow)
        print(cyan + "[3] Reports" + cyan)
        print(header + "[4] Quit" + header)
        menu_selection = input(white + '\nType [option] and press ENTER :' + white)
        return menu_selection

    def main_menu_extra(current_tournament, current_round):
        print(white + "Ready to go to the next round ?" + white)
        print("round:" + str(current_round["round_id"] + 1))
        print(green + "[1] YES" + green)
        print(header + "[2] EXIT" + header)

    def input_prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    def input_prompt():
        print("\nType [option] and press Enter : ", end='')
