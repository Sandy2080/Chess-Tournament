from tinydb import TinyDB, Query, where
from datetime import datetime, timedelta

class Database:

    def __init__(self):
        pass

    def insert_player_to_db(self, player):
        """Save new player to database """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        players_db.all()
        player_id = len(players_db.all()) + 1
        players_db.insert({
            "id": player_id,
            "last":  player["last"],
            "first": player["first"],
            "dob": player["dob"],
            "score": 0,
        })

    def load_players_db(self):
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json')
        _all = players_db.all()
        players = []
        for item in _all:
            players.append(item)
        return players

    def remove_records(self, players):
        players_db = TinyDB('data/players.json')
        for player in players:
            players_db.remove(where('first') == player["first"])
        return players_db.all()

    def update_player_score(self, player):
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        _player = Query()
        players_db.update({"score": player["score"]}, player["id"] == _player.id)

    def load_round_db(self):
        """Load rounds database
        @return: list of rounds
        """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        rounds_db.all()
        rounds = []
        for item in rounds_db:
            rounds.append(item)
        return rounds

    def load_last_round(self):
        """Load rounds database
        @return: list of rounds
        """
        return self.load_round_db()[-1]

    def load_pairs(self):
        """Load rounds database
        @return: list of rounds
        """
        return self.load_last_round()["pairs"]

    def save_tournament_to_db(self, informations, pairs):
        """Save new tournament to database """
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        round_id = len(self.load_round_db()) + 1
        tournaments_db.insert({
            "tournament_id": informations["tournament_id"],
            "name": informations["name"],
            "location": informations["location"],
            "starting_date": informations["starting_date"],
            "ending_date": informations["ending_date"],
            "rounds_total": 4,
            "current_round": round_id,
            "description": informations["description"],
            "players": pairs,
        })
        return informations["tournament_id"]

    def load_tournament_db(self):
        """Save new tournament to database """
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        return tournaments_db.all()

    def update_tournament_db(self, tournament_id, round_id):
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        tournament = Query()
        tournaments_db.update({"current_round": str(round_id)}, tournament.id == tournament_id)

    def save_round_to_db(self, tournament_id, pairs):
        """Save new player to database """
        tournaments = self.load_tournament_db()
        tournament = tournaments[tournament_id - 1]
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        round_id = len(rounds_db.all()) + 1
        round_id = rounds_db.insert({
            "tournament_id": tournament_id,
            "round_id": round_id,
            "starting_date": tournament["starting_date"],
            "starting_time":  datetime.now().strftime("%H:%M"),
            "ending_time":  (datetime.now() + timedelta(minutes=30)).strftime("%H:%M"),
            "pairs": pairs
        })
        return round_id
