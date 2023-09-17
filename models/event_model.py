import datetime


class Event:
    def __init__(self,
                 event_name: str,
                 event_location: str,
                 event_start_date: datetime,
                 event_end_date: datetime,
                 event_current_round: int,
                 event_round_list: [],
                 event_registered_players: [],
                 event_general_notes: str,
                 event_rounds=4
                 ):
        self.event_name = event_name
        self.event_location = event_location
        self.event_start_date = event_start_date
        self.event_end_date = event_end_date
        self.event_current_round = event_current_round
        self.event_round_list = event_round_list
        self.event_registered_players = event_registered_players
        self.event_general_notes = event_general_notes
        self.event_rounds = event_rounds

    def __str__(self):
        return f"Event name: {self.event_name}\nEvent Location: {self.event_location}\n" \
               f"Event Start Date: {self.event_start_date}\nEvent End Date: {self.event_end_date}\n" \
               f"Event Current Round: {self.event_current_round}\nEvent Round List: {self.event_round_list}\n" \
               f"Event Registered Players: {self.event_registered_players}\n" \
               f"Event's General Notes: {self.event_general_notes}\n"
