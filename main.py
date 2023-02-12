from Models.Player import Player

def main():
    player = Player("Sandy", "L", "DD/MM/YY", 0)
    player.save_to_db()
    print(player)

if __name__ == "__main__":
    main()