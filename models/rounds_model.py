import datetime


class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = 1
        self.rounds = []
        self.players = []
        self.general_remarks = ""

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date}) at {self.location}"

    def add_player(self, player):
        self.players.append(player)

    def start_round(self):
        if self.current_round <= self.num_rounds:
            round_name = f"Round {self.current_round}"
            start_time = datetime.datetime.now()
            new_round = {"name": round_name, "start_time": start_time, "matches": []}
            self.rounds.append(new_round)
            self.current_round += 1

    def end_round(self, round_index):
        end_time = datetime.datetime.now()
        self.rounds[round_index]["end_time"] = end_time

    def add_match(self, round_index, player1, player2):
        match = {"player1": player1, "player2": player2, "score1": 0, "score2": 0}
        self.rounds[round_index]["matches"].append(match)

    def update_match_score(self, round_index, match_index, score1, score2):
        self.rounds[round_index]["matches"][match_index]["score1"] = score1
        self.rounds[round_index]["matches"][match_index]["score2"] = score2
        self.players[self.players.index(match["player1"])].update_points(score1)
        self.players[self.players.index(match["player2"])].update_points(score2)

