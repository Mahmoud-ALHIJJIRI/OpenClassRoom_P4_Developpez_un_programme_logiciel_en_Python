from controllers.main_controller import MainController
from models.players_model import Player


class PlayerController:
    def __init__(self):
        self.running_player = MainController()
        self.players = []

    def handle_player_menu(self, player_choice):
        while True:
            if player_choice == "1":
                self.add_player()
                break
            elif player_choice == "2":
                print("List Players")
                break
            elif player_choice == "3":
                print("return to main menu")
                break
            elif player_choice == "0":
                self.running_player.running = False
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
                player_choice = input("Enter your choice: ")

    def add_player(self):
        print("Add New Player")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        birth_date = input("Enter Birth Date: ")
        chess_id = input("Enter Chess ID: ")

        new_player = Player(first_name, last_name, birth_date, chess_id)
        self.players.append(new_player)

        print("Player added successfully!")

