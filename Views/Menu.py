class MenuView:

    def __init__(self):
        pass

    def start():
        print("\n\n----------------------------------")
        print("        CHESS TOURNAMENTS")
        print("----------------------------------")
    
    def main_menu():
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Create new tournament")
        print("[2] Create new player")
        print("[3] Reports")
    
    def main_menu_extra(name):
        print("\n\n=== MAIN MENU ===\n")
        print("[1] Resume tournament " + name)
        print("[2] Create new tournament")
        print("[3] Create new player")
        print("[4] Reports")

    def input_prompt_text(option):
        print(f"\nEnter {option} (type [back] for main menu) : ", end='')

    def input_prompt():
        print("\nType [option] and press Enter : ", end='')
    
    