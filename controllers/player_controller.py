from models.players_model import Player
import json
import datetime
import os


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%d/%m/%Y')
        return super().default(obj)


class PlayerController:
    def __init__(self):
        self.players = self.load_players_from_json()

    def handle_player_menu(self, player_choice):

        while True:
            if player_choice == "1":
                self.add_player()
                break
            elif player_choice == "2":
                self.list_players()
                break
            elif player_choice == "3":
                print("Returning to the main menu.")
                break
            elif player_choice == "0":
                print("Exiting the application.")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")
                break

    def add_player(self):
        while True:
            print("Add New Player")
            first_name = input("Enter First Name or( '9' to go to main menu, 'exit' to quit): ").title()

            if first_name.lower() == 'exit':
                exit()
            if first_name == '9':
                break

            last_name = input("Enter Last Name or( '9' to go to main menu, 'exit' to quit): ").upper()

            if last_name.lower() == 'exit':
                exit()
            if first_name == '9':
                break
            date_of_birth = None
            while True:
                birth_date_str = input("Enter Birth Date (dd/mm/yyyy) or( '9' to go to main menu, 'exit' to quit): ")

                if birth_date_str.lower() == 'exit':
                    exit()
                if birth_date_str == '9':
                    break

                try:
                    date_of_birth = datetime.datetime.strptime(birth_date_str, '%d/%m/%Y').date()
                    break
                except ValueError:
                    print("Invalid date format. Please use dd/mm/yyyy format.")

            chess_id = self.generate_player_id()

            new_player = Player(first_name, last_name, date_of_birth, chess_id, opponents=[])
            self.players.append(new_player)
            self.save_players_to_json()

            print(f"The Player:\n{new_player.chess_id} {new_player.first_name} {new_player.last_name} "
                  f"{date_of_birth}\nhas been added successfully!")

            while True:
                print("Choose an option:")
                print("1. Add another player")
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

    def generate_player_id(self):
        existing_ids = [int(player.chess_id[2:]) for player in self.players]

        if not existing_ids:
            new_id = "AA001"
        else:
            max_existing_id = max(existing_ids)
            new_id = f"AA{max_existing_id + 1:03d}"

        return new_id

    @staticmethod
    def load_players_from_json():
        players_data = []

        file_path = os.path.join('database', 'Players.json')

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    players_data = json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error loading player data from JSON: {e}")

        return [Player(
            first_name=player_data.get('first_name', ''),
            last_name=player_data.get('last_name', ''),
            date_of_birth=player_data.get('date_of_birth', datetime.date.today()),
            chess_id=player_data.get('chess_id', ''),
            opponents=[],
            score=player_data.get('score', 0),
        )
            for player_data in players_data]

    def save_players_to_json(self):
        players_data = [player.__dict__ for player in self.players]
        folder_path = 'database'
        file_path = os.path.join(folder_path, 'Players.json')

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(file_path, 'w') as file:
            json.dump(players_data, file, cls=DateEncoder, indent=2)

    def list_players(self):
        if not self.players:
            print("No players found.")
        else:
            print("Listing Players")
            sorted_players = sorted(self.players,
                                    key=lambda player_sort: (player_sort.last_name, player_sort.first_name))
            for player in sorted_players:
                print(f"ID: {player.chess_id}, Full Name: {player.first_name} {player.last_name}, "
                      f"Score: {player.score}")
