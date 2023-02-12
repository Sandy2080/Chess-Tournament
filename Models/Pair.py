class Pair:
    """Couple de joueur"""
    
    def __init__(self, _player1, _player2):
        """Initialise les pairs de joueur"""
        self.id = _player1.name + _player2.name
        self.player1 = _player1
        self.player2 = _player2