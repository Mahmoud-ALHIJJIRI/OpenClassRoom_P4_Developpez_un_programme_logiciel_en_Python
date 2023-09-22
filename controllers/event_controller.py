import datetime
import json
import os
from models.event_model import Event
from views.main_view import MenuView
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from models.rounds_model import Round
from models.players_model import Player


class EventController:
    def __init__(self):
        self.events = self.load_event_from_json()
        self.event_view = MenuView()
        self.players_list = PlayerController()
        self.rounds = RoundController()

    def handle_event_menu(self, event_choice):

        if event_choice == "1":
            print("Add a new Event")
            self.add_new_event()
        elif event_choice == "2":
            print("Listing Events")
            self.list_events()
        elif event_choice == "3":
            print("Managing an Event")
            self.select_event_to_mange()
        elif event_choice == "4":
            print("Returning to Main Menu")
        elif event_choice == "0":
            print("Exiting the application")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

    def add_new_event(self):
        while True:
            event_name = input("Enter Event Name or( '9' to go to main menu, 'exit' to quit): ").title()
            if event_name.lower() == 'exit':
                exit()
            if event_name == '9':
                break
            event_location = input("Enter Event's Location or( '9' to go to main menu, 'exit' to quit): ").title()
            if event_location.lower() == 'exit':
                exit()
            if event_location == '9':
                break
            while True:
                event_start_date = input("Enter Event's Start Date (dd/mm/yyyy) "
                                         "or( '9' to go to main menu, 'exit' to quit): ")
                if event_start_date.lower() == 'exit':
                    exit()
                if event_start_date == '9':
                    break
                try:
                    event_start_date = datetime.datetime.strptime(event_start_date, '%d/%m/%Y').date()
                    break
                except ValueError:
                    print("Invalid date format. Please use dd/mm/yyyy format.")
            while True:
                event_end_date = input("Enter Event's End Date (dd/mm/yyyy) "
                                       "or( '9' to go to main menu, 'exit' to quit): ")
                if event_end_date.lower() == 'exit':
                    exit()
                if event_end_date == '9':
                    break
                try:
                    event_end_date = datetime.datetime.strptime(event_end_date, '%d/%m/%Y').date()
                    break
                except ValueError:
                    print("Invalid date format. Please use dd/mm/yyyy format.")

            event_current_round = 1
            event_round_list = []
            event_registered_players = []

            event_general_notes = input("Enter Event's General Notes or( '9' to go to main menu, 'exit' to quit): ")
            if event_general_notes == 'exit':
                exit()
            if event_general_notes == '9':
                break

            new_event = Event(event_name, event_location, event_start_date, event_end_date,
                              event_current_round, event_round_list, event_registered_players, event_general_notes)
            self.events.append(new_event)
            self.save_event_to_json()
            print(f"The Event:\n{new_event.event_name} in {new_event.event_location}"
                  f"\nhas been added successfully!")
            while True:
                print("Choose an option:")
                print("1. Add another Event")
                print("2. Return to the main menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    # Continue adding another player
                    break
                elif choice == "2":
                    # Return to the main menu
                    return
                else:
                    print("Invalid choice. Please select a valid option.")

    @staticmethod
    def load_event_from_json():
        events_data = []
        file_path = os.path.join('database', 'events.json')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    events_data = json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error loading event data from JSON: {e}")

        events = []
        for event_data in events_data:
            event = Event(
                event_name=event_data['event_name'],
                event_location=event_data['event_location'],
                event_start_date=datetime.datetime.strptime(event_data['event_start_date'], '%Y-%m-%d').date(),
                event_end_date=datetime.datetime.strptime(event_data['event_end_date'], '%Y-%m-%d').date(),
                event_current_round=event_data['event_current_round'],
                event_round_list=event_data['event_round_list'],
                event_registered_players=event_data['event_registered_players'],
                event_general_notes=event_data['event_general_notes'],
                event_rounds=event_data.get('event_rounds', 4)
            )

            round_data_list = event_data['event_round_list']
            rounds = []
            for round_data in round_data_list:
                round_obj = Round(
                    name=round_data['name'],
                    start_time=datetime.datetime.strptime(round_data['start_time'], '%Y-%m-%d %H:%M:%S'),
                    end_time=datetime.datetime.strptime(round_data['end_time'], '%Y-%m-%d %H:%M:%S') if round_data[
                        'end_time'] else None,
                    matches=[]
                )
                rounds.append(round_obj)
            event.event_round_list = rounds

            # Deserialize player data and append player objects to event_registered_players
            player_data_list = event_data['event_registered_players']
            players = []
            for player_data in player_data_list:
                player = Player(
                    first_name=player_data['first_name'],
                    last_name=player_data['last_name'],
                    date_of_birth=player_data['date_of_birth'],
                    chess_id=player_data['chess_id'],
                    score=player_data['score']
                )
                players.append(player)
            event.event_registered_players = players

            events.append(event)

        return events

    def save_event_to_json(self):
        events_data = []
        folder_path = 'database'
        file_path = os.path.join(folder_path, 'events.json')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for event in self.events:
            round_data = []
            for round_obj in event.event_round_list:
                matches_data = [match.to_dict() for match in round_obj.matches]
                round_data.append({
                    'name': round_obj.name,
                    'start_time': round_obj.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_time': round_obj.end_time.strftime('%Y-%m-%d %H:%M:%S') if round_obj.end_time else None,
                    'matches': matches_data
                })

            players_data = [player.to_dict() for player in event.event_registered_players]

            event_data = {
                'event_name': event.event_name,
                'event_location': event.event_location,
                'event_start_date': event.event_start_date.strftime('%Y-%m-%d'),
                'event_end_date': event.event_end_date.strftime('%Y-%m-%d'),
                'event_current_round': event.event_current_round,
                'event_round_list': round_data,  # Serialize rounds as dictionaries
                'event_registered_players': players_data,
                'event_general_notes': event.event_general_notes,
                'event_rounds': event.event_rounds
            }
            events_data.append(event_data)

        with open(file_path, 'w') as file:
            json.dump(events_data, file, indent=2)

    def list_events(self):
        if not self.events:
            print("No events found.")
        else:
            print("List of Events:")
            for i, event in enumerate(self.events, start=1):
                print(f"{i}. {event.event_name} in {event.event_location}")

    def select_event_to_mange(self):
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
                        self.manage_selected_event(selected_event)
                        break
                    else:
                        print("Invalid event number. Please enter a valid number or 'exit' to quit.")
                except ValueError:
                    print("Invalid input. Please enter a number or 'exit' to quit.")

    def manage_selected_event(self, selected_event):
        print(f"***Managing", selected_event.event_name, "***")
        self.event_view.one_event_manage_menu()
        while True:

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_players_to_event(selected_event)
                break
            elif choice == "2":
                self.list_registered_players(selected_event)
                break
            elif choice == "3":
                self.manage_rounds(selected_event)
                break
            elif choice == "4":
                self.view_general_notes(selected_event)
            elif choice == "5":
                print("Returning to the previous menu")
                break
            elif choice == "0":
                print("Exiting the Application")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def add_players_to_event(self, selected_event):
        while True:
            players_available = self.players_list.load_players_from_json()

            if not players_available:
                print("No Players available to add!")
                return  # Exit the method if no players are available

            print("Here are the players available to add:")
            print()
            for player in players_available:
                print(f"Player ID: {player.chess_id}, Name: {player.first_name} {player.last_name}")

            player_choice = input("Enter the chess ID of the player you want to add (or 'exit' to quit): ")
            player_choice = player_choice.strip()

            if player_choice.lower() == 'exit':
                exit()
            elif player_choice not in [player.chess_id for player in players_available]:
                print("Invalid player ID. Please enter a valid chess ID from the list.")
            else:
                selected_player = next((player for player in players_available
                                        if player.chess_id == player_choice), None)
                if selected_player:
                    if selected_player.chess_id in \
                            [player.chess_id for player in selected_event.event_registered_players]:
                        print(f"The player with ID {player_choice} is already registered for the event.")
                    else:
                        selected_event.event_registered_players.append(selected_player)
                        print(f"The player with ID {player_choice} has been added to the event.")
                        self.save_event_to_json()
                else:
                    print("Player not found in the available players list.")

            while True:
                print("Choose an option:")
                print("1. Add another player to the Event")
                print("2. Return to the main menu")

                choice = input("Enter your choice: ")

                if choice == "1":
                    break
                elif choice == "2":
                    return
                else:
                    print("Invalid choice. Please select a valid option.")

    @staticmethod
    def list_registered_players(selected_event):
        if not selected_event.event_registered_players:
            print("No players registered for this event.")
        else:
            print("List of Registered Players for Event:")
            for player in selected_event.event_registered_players:
                print(f"Player ID: {player.chess_id}, Name: {player.first_name} {player.last_name}")

    def manage_rounds(self, selected_event):
        while True:
            self.event_view.rounds_manager_menu()
            selected_option = input("Enter your choice: ")

            if selected_option == "1":
                print("Add a new Round to the event")
                self.add_new_round(selected_event)
                break
            elif selected_option == "2":
                print("Listing Event's Rounds")
                self.list_event_rounds(selected_event)
                break
            elif selected_option == "3":
                print("Managing a Round in this Event")
                self.select_round_to_manage()
            elif selected_option == "4":
                print("Returning to Main Menu")
            elif selected_option == "0":
                print("Exiting the application")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def add_new_round(self, selected_event):
        max_rounds = 4
        round_name_template = "Round {}"

        while len(selected_event.event_round_list) < max_rounds:
            new_round_name = round_name_template.format(len(selected_event.event_round_list) + 1)

            while True:
                start_datetime_str = input(
                    f"Enter the start date and time for '{new_round_name}' (DD/MM/YYYY HH:MM): ").strip()
                try:
                    start_datetime = datetime.datetime.strptime(start_datetime_str, '%d/%m/%Y %H:%M')

                    end_datetime_str = input(
                        f"Enter the end date and time for '{new_round_name}' (DD/MM/YYYY HH:MM): ").strip()
                    try:
                        end_datetime = datetime.datetime.strptime(end_datetime_str, '%d/%m/%Y %H:%M')
                        break
                    except ValueError:
                        print("Invalid date and time format. Please use DD/MM/YYYY HH:MM format.")
                except ValueError:
                    print("Invalid date and time format. Please use DD/MM/YYYY HH:MM format.")

            new_round = Round(new_round_name, start_datetime, end_datetime, matches=[])

            # Add the new round to the event's round list
            selected_event.event_round_list.append(new_round)

            print(f"New round '{new_round_name}' has been added to the event.")

            choice = input(
                "Choose an option:\n1. Add another Round to the Event\n2. Return to the main menu\nEnter your choice: ")

            if choice == "2":
                break
            elif choice != "1":
                print("Invalid choice. Please select a valid option.")
        else:
            print("The maximum number of rounds has been reached")

        self.save_event_to_json()

    @staticmethod
    def list_event_rounds(selected_event):
        if not selected_event.event_round_list:
            print("No Rounds entered for this event")
        else:
            print(f"List of Rounds for Event '{selected_event.event_name}':")
            for event_round in selected_event.event_round_list:
                print(f"The Round: {event_round.name} - Start Time: {event_round.start_time} - "
                      f"End Time: {event_round.end_time}")

    def select_round_to_manage(self):
        pass

    @staticmethod
    def view_general_notes(selected_event):
        if selected_event.event_general_notes:
            print(f"General Notes for Event '{selected_event.event_name}':")
            print(selected_event.event_general_notes)
        else:
            print(f"No general notes available for Event '{selected_event.event_name}'.")
