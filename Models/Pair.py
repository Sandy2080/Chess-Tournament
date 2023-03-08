class Pair:
    """Couple de joueur"""

    def __init__(self, player1: str, player2: str):
        """Initialise les pairs de joueur"""
        self.id = player1.name + player2.name
        self.player1 = player1
        self.player2 = player2