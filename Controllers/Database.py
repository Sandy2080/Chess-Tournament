from tinydb import TinyDB, Query, where
from datetime import date
from time import gmtime, strftime


class Database:

    def insert_player_to_db(self, player):
        """Save new player to database """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        players_db.all()
        player_id = len(players_db.all()) + 1
        players_db.insert({
            "id": player["id"] if player["id"] != "" else player_id,
            "last":  player["last"],
            "first": player["first"],
            "dob": player["dob"],
            "score": player["score"],
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

    def insert_records(self, players):
        for player in players:
            self.insert_player_to_db(player)

    def update_player_score(self, player):
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('data/players.json', indent=4, separators=(',', ': '))
        _player = Query()
        players_db.update({"score": player["score"]}, player["id"] == _player.id)

    def save_tournament_to_db(self, informations, pairs):
        """Save new tournament to database """
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        tournaments_db.all()
        tournament_id = len(tournaments_db.all()) + 1
        tournaments_db.insert({
            "id": tournament_id,
            "name": informations["name"],
            "location": informations["location"],
            "starting_date": informations["starting_date"],
            "ending_date": informations["ending_date"],
            "current_round": 0,
            "players": pairs,
            "description": informations["description"]
        })
        print
        return tournament_id

    def update_tournament_db(self, tournament_id, round_id):
        tournaments_db = TinyDB('data/tournaments.json', indent=4, separators=(',', ': '))
        tournament = Query()
        tournaments_db.update({"current_round": str(round_id)}, tournament.id == tournament_id)

    def save_round_to_db(self, tournament_id, pairs):
        """Save new player to database """
        rounds_db = TinyDB('data/rounds.json', indent=4, separators=(',', ': '))
        rounds_db.all()
        round_id = len(rounds_db.all()) + 1
        round_id = rounds_db.insert({
            "tournament_id": tournament_id,
            "round_id": round_id,
            "starting_date": str(date.today()),
            "ending_date": "",
            "starting_time":  str(strftime("%H:%M", gmtime())),
            "ending_time": "",
            "pairs": pairs
        })
        return round_id
