import Players


class Event:
    def __init__(self, event_name, event_location, event_start_date, event_end_date, general_notes, event_rounds=4):
        self.event_name = event_name
        self.event_location = event_location
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_current_round = 1
        self.event_round_list = []
        self.event_registered_players = []
        self.general_notes = general_notes
        self.event_rounds = event_rounds

    def __str__(self):
        return f"Even_name: {self.event_name}\nEvent Location: {self.event_location}\n" \
               f"Event Start Date: {self.event_start_date}\nEvent End Date: {self.event_end_date}\n" \
               f"Event Current Round: {self.event_current_round}\nEvent Round List: {self.event_round_list}\n" \
               f"Event Registered Players: {self.event_registered_players}\nGeneral Notes: {self.general_notes}\n" \
               f"Event Rounds: {self.event_rounds}\n"

    def add_player(self, player):
        self.event_registered_players.append(player)


event_test = Event("CDG", "Paris", "01-01-2023", "31-01-2023", "high competition")
player1 = Players.Player("Mahmoud", "ALHIJJIRI", "11 March 1990", "AA007")
player2 = Players.Player("Mahm", "ALHIJ", "11 March 1990", "AA008")

event_test.add_player(player1)
event_test.add_player(player2)


print(event_test)
print(player2, player1, sep="")
