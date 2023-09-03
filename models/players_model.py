class Player:
    def __init__(self, first_name, last_name, birth_date, chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.total_points = 0

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nBirth Date: {self.birth_date}\n" \
               f"ID: {self.chess_id}\n"


player1 = Player("Mahmoud", "ALHIJJIRI", "11 March 1990", "AA007")


print(player1)
