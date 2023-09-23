import datetime
from typing import List


class Match:
    def __init__(self, player1, player2, result=None):
        self.player1 = player1
        self.player2 = player2
        self.result = result

    def to_dict(self):
        return {
            'player1': self.player1.to_dict(),
            'player2': self.player2.to_dict(),
            'result': self.result.to_dict()
        }


class Round:
    def __init__(self, name: str, start_time: datetime, end_time: datetime, matches: List[Match]):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches
