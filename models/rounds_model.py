import datetime


class Round:
    def __init__(self, name: str, start_time: datetime, end_time: datetime):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = []

    def add_match(self, player1, player2):
        match = Match(player1, player2)
        self.matches.append(match)


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None
