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


# Example usage
if __name__ == "__main__":
    tournament = Tournament("Chess Tournament", "City Hall", "2023-08-15", "2023-08-20")

    player1 = Player("John", "Doe", "1990-05-15", "AB12345")
    player2 = Player("Jane", "Smith", "1985-12-10", "CD67890")

    tournament.add_player(player1)
    tournament.add_player(player2)

    tournament.start_round()
    tournament.add_match(0, player1, player2)
    tournament.update_match_score(0, 0, 1, 0.5)

    print(tournament)
    print(tournament.rounds)
    print(player1)
    print(player2)
