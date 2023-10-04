import datetime
from views.main_view import MenuView
from models.rounds_model import Round
from controllers.matchs_controller import MatchesController


class RoundController:
    def __init__(self):
        self.event_view = MenuView()
        self.matches_controller = MatchesController

    def add_new_round(self, selected_event):
        round_name_template = "Round {}"
        current_round_terminated = True
        max_rounds = 4
        if len(selected_event.event_round_list) >= max_rounds:
            print(f"The maximum number of rounds for {selected_event.event_name} has been reached.")
            exit()
        new_round = None
        new_round_name = ""

        if len(selected_event.event_round_list) > 0:
            current_round_number = len(selected_event.event_round_list)
            print(f"The current round ({current_round_number}) has been terminated.")
            if selected_event.event_current_round < 4:
                selected_event.event_current_round += 1

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
                    self.matches_controller.generate_matches(selected_event)

                    self.event_view.round_options()
            choice = input("Enter your choice: ")
            if choice == "1":
                new_round.end_time = datetime.datetime.now()
                if selected_event.event_current_round < 4:
                    selected_event.event_current_round += 1
                print(f"Round '{new_round_name}' has been terminated at "
                      f"{new_round.end_time.strftime('%H:%M on %d-%m-%Y')}.")
                current_round_terminated = True

            elif choice == "9":
                break
            elif choice == "0":
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
                start_time_str = event_round.start_time.strftime('%H:%M on %d-%m-%Y')
                if event_round.end_time is not None:
                    end_time_str = event_round.end_time.strftime('%H:%M on %d-%m-%Y')
                else:
                    end_time_str = "This Round is still going on!"

                print(f"The Round: {event_round.name} - "
                      f"Start Time: {start_time_str} - "
                      f"End Time: {end_time_str}")
