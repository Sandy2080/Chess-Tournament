
class MenuPlayerView:

    def __init__(self):
        pass

    def start():
        print("\n\n=== Create Player ? ===\n")
        print("[1] save")
        print("[2] cancel")


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
