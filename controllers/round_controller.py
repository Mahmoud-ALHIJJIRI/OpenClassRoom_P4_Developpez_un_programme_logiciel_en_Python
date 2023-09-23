import datetime
import random
from views.main_view import MenuView
from models.rounds_model import Round, Match


class RoundController:
    def __init__(self):
        self.event_view = MenuView()

    def add_new_round(self, selected_event):
        round_name_template = "Round {}"

        current_round_terminated = True
        max_rounds = 4

        new_round = None
        new_round_name = ""

        if len(selected_event.event_round_list) > 0:
            current_round_number = len(selected_event.event_round_list) + 1
            print(f"The current round ({current_round_number}) has been terminated.")

        while True:
            if len(selected_event.event_round_list) >= max_rounds:
                print("The maximum number of rounds has been reached.")
                break

            if current_round_terminated:
                new_round_name = round_name_template.format(len(selected_event.event_round_list) + 1)

                # Check if a round with the same name already exists
                if any(round_exist.name == new_round_name for round_exist in selected_event.event_round_list):
                    print(f"Round '{new_round_name}' already exists.")
                else:
                    start_datetime = datetime.datetime.now()
                    end_datetime = None  # Initialize end_datetime as None for the new round

                    new_round = Round(new_round_name, start_datetime, end_datetime, matches=[])

                    # Add the new round to the event's round list
                    selected_event.event_round_list.append(new_round)

                    print(f"New round '{new_round_name}' has been started at "
                          f"{start_datetime.strftime('%H:%M on %d-%m-%Y')} in the event {selected_event.event_name}.")
                    current_round_terminated = False  # Set the flag to indicate that a round is in progress

            choice = input(
                "Choose an option:\n1. Create Matches for this Round.\n2. Terminate current Round and start next Round"
                "\n9. Return to the main menu\nEnter your choice: ")
            if choice == "1":
                self.generate_matches(selected_event)
            elif choice == "2":
                new_round.end_time = datetime.datetime.now()
                print(f"Round '{new_round_name}' has been terminated at "
                      f"{new_round.end_time.strftime('%H:%M on %d-%m-%Y')}.")
                current_round_terminated = True
            elif choice == "9":
                break
            else:
                print("Invalid choice. Please select a valid option.")

    @staticmethod
    def list_event_rounds(selected_event):
        if not selected_event.event_round_list:
            print("No Rounds entered for this event")
        else:
            print(f"List of Rounds for Event '{selected_event.event_name}':")
            for event_round in selected_event.event_round_list:
                start_time_str = event_round.start_time.strftime('%H:%M on %d-%m-%Y')
                if event_round.end_time is not None:
                    end_time_str = event_round.end_time.strftime('%H:%M on %d-%m-%Y')
                else:
                    end_time_str = "This Round is still going on!"

                print(f"The Round: {event_round.name} - "
                      f"Start Time: {start_time_str} - "
                      f"End Time: {end_time_str}")

    @staticmethod
    def generate_matches(selected_event):
        sorted_players = sorted(selected_event.event_registered_players,
                                key=lambda x: (-x.score, x.first_name, x.last_name))

        round_number = selected_event.event_current_round
        previous_round_matches = selected_event.event_round_list[round_number - 2].matches if round_number > 1 else None

        matches = []

        if round_number == 1:
            random.shuffle(sorted_players)
            match_counter = 1  # Changed match_counter to start from 1

            for i in range(0, len(sorted_players), 2):
                match_id = f"{selected_event.event_name} - Round{selected_event.event_current_round} - " \
                           f"M{match_counter:02d}"
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1] if i + 1 < len(sorted_players) else None
                match = Match(match_id, player1, player2)
                matches.append(match)
                match_counter += 1

        # Get the current round
        current_round = selected_event.event_round_list[round_number - 1]

        # Append the matches to the current round's matches attribute
        current_round.matches.extend(matches)

        print("Matches generated and stored in the current round.")
        for match in matches:
            print(f"Match ID: {match.match_id}")
            print(f"Player 1: {match.player1.first_name} {match.player1.last_name}")
            print(f"Player 2: {match.player2.first_name} {match.player2.last_name}")
