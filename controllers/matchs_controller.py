import random

from controllers.round_controller import RoundController
from models.rounds_model import Match


class MatchesController:
    def __init__(self):
        self.round_controller = RoundController()

    def select_round_to_manage(self, selected_event):
        while True:
            if not selected_event.event_round_list:
                print("No rounds available for this event.")
                return
            self.round_controller.list_event_rounds(selected_event)
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
                print("Generate matches for this Round")
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
                match_id = f"{selected_event.event_name} - Round {round_number} - M{i + 1:02d}"
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1] if i + 1 < len(
                    sorted_players) else None  # Handles odd number of players
                match = Match(match_id, player1, player2)
                matches.append(match)
        elif round_number > 1:
            used_players = set()
            previous_opponents = {player: set() for player in sorted_players}
            player_index = 0

            for previous_match in previous_round_matches:
                player1, player2 = previous_match.player1, previous_match.player2
                previous_opponents[player1].add(player2)
                previous_opponents[player2].add(player1)

            match_counter = 1
            for player in sorted_players:
                if player not in used_players:
                    used_players.add(player)

                    while True:
                        opponent = sorted_players[player_index]

                        if player not in previous_opponents[opponent]:
                            break

                        player_index = (player_index + 1) % len(sorted_players)

                    match_id = f"{selected_event.event_name} - Round {round_number} - M{match_counter:02d}"
                    match = Match(match_id, player, opponent)
                    matches.append(match)
                    match_counter += 1

        for match in matches:
            print(f"Match ID: {match.match_id}")
            print(f"Player 1: {match.player1.first_name} {match.player1.last_name}")
            print(f"Player 2: {match.player2.first_name} {match.player2.last_name}")
