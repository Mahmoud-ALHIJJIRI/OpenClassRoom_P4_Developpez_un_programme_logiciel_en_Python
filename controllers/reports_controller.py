from controllers.event_controller import EventController
from views.main_view import MenuView
from controllers.round_controller import RoundController
from controllers.player_controller import PlayerController


class ReportController:
    def __init__(self):
        self.event_controller = EventController()
        self.events = EventController.load_event_from_json()
        self.view = MenuView()
        self.round_controller = RoundController()
        self.player_controller = PlayerController()

    def handle_report_menu(self, report_choice):

        while True:
            if report_choice == "1":
                self.player_controller.list_players()
                break
            elif report_choice == "2":
                self.event_controller.list_events()
                break
            elif report_choice == "3":
                self.select_event_to_get_reports()
                break
            elif report_choice == "9":
                print("Returning to main menu")
                break
            elif report_choice == "0":
                print("Exiting the application")
                exit()
            else:
                print("Invalid choice. Please select a valid option")

    def select_event_to_get_reports(self):
        while True:
            if not self.events:
                print("No events found.")
            else:
                print("List of Events:")
                for i, event in enumerate(self.events, start=1):
                    print(f"{i}. {event.event_name} - {event.event_location}")

                try:
                    choice = input("Enter the number of the event you want to select "
                                   "or( '9' to go to main menu, 'exit' to quit): ")
                    if choice.lower() == 'exit':
                        exit()
                    if choice == '9':
                        break
                    choice = int(choice)
                    if 1 <= choice <= len(self.events):
                        selected_event = self.events[choice - 1]
                        print(f"You selected event: {selected_event.event_name}")
                        self.reports_selected_event(selected_event)
                        break
                    else:
                        print("Invalid event number. Please enter a valid number or 'exit' to quit.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'exit' to quit.")

    def reports_selected_event(self, selected_event):
        print(f"***Managing", selected_event.event_name, "***")
        self.view.one_event_reports_menu()
        while True:

            choice = input("Enter your choice: ")
            if choice == "1":
                self.event_details(selected_event)
                break
            elif choice == "2":
                self.event_controller.list_registered_players(selected_event)
                break
            elif choice == "3":
                self.round_controller.list_event_rounds(selected_event)
                break
            elif choice == "4":
                self.list_event_matches(selected_event)
            elif choice == "9":
                print("Returning to the previous menu")
                break
            elif choice == "0":
                print("Exiting the Application")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    @staticmethod
    def event_details(selected_event):
        print(f"{selected_event.event_name} starts on {selected_event.event_start_date} "
              f"Ends on {selected_event.event_end_date}")

    @staticmethod
    def list_event_matches(selected_event):
        has_matches = False  # Flag to check if there are matches

        for round_obj in selected_event.event_round_list:
            print(f"Round: {round_obj.name}")
            for match in round_obj.matches:
                print(f"Match ID: {match.match_id}")
                print(f"Player 1: {match.player1.first_name} {match.player1.last_name}")
                print(f"Player 2: {match.player2.first_name} {match.player2.last_name}")
                print(f"Result: {match.result}")
                print()
                has_matches = True  # Set the flag to True since there are matches

        if not has_matches:
            print("No matches found for this event.")


