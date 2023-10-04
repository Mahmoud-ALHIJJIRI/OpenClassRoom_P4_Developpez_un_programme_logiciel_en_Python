import datetime
from typing import List


class Match:
    def __init__(self, match_id, player1, player2, result=None):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.result = result

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'player1': self.player1.to_dict(),
            'player2': self.player2.to_dict(),
            'result': self.result
        }


class Round:
    def __init__(self, name: str, start_time: datetime, end_time: datetime, matches: List[Match]):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.matches = matches

    def print_match(self):
        for m in self.matches:
            print(m)
