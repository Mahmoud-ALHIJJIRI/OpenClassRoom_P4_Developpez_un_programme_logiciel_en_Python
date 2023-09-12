import datetime


class Player:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 date_of_birth: datetime,
                 chess_id: str,
                 score=0
                 ):
        """ Initialize the player. By's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        self.score = score
        self.opponents = []

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}\nBirth Date: {self.date_of_birth}\n" \
               f"ID: {self.chess_id}\n"


