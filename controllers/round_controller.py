import datetime
import random
from views.main_view import MenuView
from models.rounds_model import Round, Match


class RoundController:
    def __init__(self):
        self.event_view = MenuView()

    def add_new_round(self, selected_event):
        round_name_template = "Round {}"

        current_round_terminated = True  # Initially, no round is in progress
        max_rounds = 4  # Maximum allowed rounds

        new_round = None  # Initialize new_round outside the if block
        new_round_name = ""  # Initialize new_round_name with a default value

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

                    print(f"New round '{new_round_name}' has been started {start_datetime} to the event.")
                    current_round_terminated = False  # Set the flag to indicate that a round is in progress

            choice = input(
                "Choose an option:\n1. Terminate current Round and start next Round"
                "\n2. Return to the main menu\nEnter your choice: ")

            if choice == "1":
                current_round_terminated = True
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please select a valid option.")
            new_round.end_datetime = datetime.datetime.now()
            print(f"Round '{new_round_name}' has been terminated.")

            self.generate_matches(selected_event)

    @staticmethod
    def generate_matches(selected_event):
        sorted_players = sorted(selected_event.event_registered_players,
                                key=lambda x: (-x.score, x.first_name, x.last_name))

        round_number = selected_event.event_current_round
        previous_round_matches = selected_event.event_round_list[round_number - 2].matches if round_number > 1 else None

        print(f"List of Registered Players for Event (Round {round_number}):")
        for i, player in enumerate(sorted_players, start=1):
            print(
                f"{i}. Player ID: {player.chess_id}, Name: {player.first_name} {player.last_name}, "
                f"Score: {player.score}")

        matches = []

        if round_number == 1:
            random.shuffle(sorted_players)

            for i in range(0, len(sorted_players), 2):
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1] if i + 1 < len(
                    sorted_players) else None  # Handles odd number of players
                match = Match(player1, player2)
                matches.append(match)
        elif round_number > 1:
            used_players = set()
            previous_opponents = {player: set() for player in sorted_players}

    def select_round_to_manage(self, selected_event):
        while True:
            if not selected_event.event_round_list:
                print("No rounds available for this event.")
                return
            self.list_event_rounds(selected_event)
            try:
                choice = input("Enter the number of the round you want to manage "
                               "or ('exit' to quite, '9' to return to the main menu): ").strip()
                if choice.lower() == 'exit':
                    exit()
                elif choice.lower() == '9':
                    return  # Return to the main menu
                else:
                    choice = int(choice)
                    if 1 <= choice <= len(selected_event.event_round_list):
                        selected_round = selected_event.event_round_list[choice - 1]
                        print(f"You selected round: {selected_round.name}")
                        self.manage_selected_round(selected_round)
                    else:
                        print("Invalid round number. Please enter a valid number or 'exit' to go back.")
            except ValueError:
                print("Invalid input. Please enter a number or 'exit' to go back.")

    def manage_selected_round(self, selected_event):
        while True:
            print("""
            What do you want to do:
            1- Add match to the Round
            2- List Matches in this Round
            3- Return to main menu
            0- Exit the Application
            """)
            round_manage_choice = input("Entre you choice: ")

            if round_manage_choice == '1':
                print("Add match to the Round")
                self.generate_matches(selected_event)
            elif round_manage_choice == '2':
                print("List Matches in this Round")

            elif round_manage_choice == '3':
                print("Returning to Main Menu")

            elif round_manage_choice == '0':
                print("Exiting the application")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    @staticmethod
    def list_event_rounds(selected_event):
        if not selected_event.event_round_list:
            print("No Rounds entered for this event")
        else:
            print(f"List of Rounds for Event '{selected_event.event_name}':")
            for event_round in selected_event.event_round_list:
                print(f"The Round: {event_round.name} - Start Time: {event_round.start_time} - "
                      f"End Time: {event_round.end_time}")
