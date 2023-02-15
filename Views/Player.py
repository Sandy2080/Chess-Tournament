from Controllers.utilities import input_text_field, date_text_field

class MenuPlayerView:

    def __init__(self):
        pass

    def start():
        print("\n\n=== Create Player ? ===\n")
        print("[1] save")
        print("[2] cancel")

    def ask_player_info(self) -> dict:
        player_informations = {}
        player_attrs = [
            "first", 
            "last", 
            "dob"
        ]
        
        for item in player_attrs:
            user_input = input().lower()
            if user_input == "back":
                self.start()
            player_informations[item.lower()] = input_text_field(item)
        return player_informations

    def display_players(players, index):
        ''' Function : select_players

            Parameters
            ----------
            players : list
                      list of players
            player_number : int
                            one player in tournament
            Returns
            ----------
            no return
        '''
        print(f"[{players[index]['id']}]", end=' ')
        print(f"{players[index]['last']}, {players[index]['first']}, {players[index]['dob']}", end=" | ")
        print(f"Score : {players[index]['score']}")
        return players[index]
