import datetime


class Player:

    def __init__(self, first_name: str, last_name: str, date_of_birth: datetime, chess_id: str, score=0):
        """ Initialize the player's attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        self.score = score
        self.opponents = []

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}\nBirth Date: {self.date_of_birth}\n" \
               f"ID: {self.chess_id}\n"

    def to_dict(self):
        """ Convert Player object to a dictionary """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'chess_id': self.chess_id,
            'score': self.score,
            'opponents': self.opponents  # You can add logic here to convert opponents to a suitable format
        }
