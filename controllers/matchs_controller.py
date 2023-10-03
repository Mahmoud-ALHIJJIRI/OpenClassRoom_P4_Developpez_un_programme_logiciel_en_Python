import random
from models.rounds_model import Match


class MatchesController:

    @staticmethod
    def generate_matches(selected_event):
        sorted_players = sorted(selected_event.event_registered_players,
                                key=lambda x: (-x.score, x.first_name, x.last_name))

        round_number = selected_event.event_current_round

        matches = []

        if round_number == 1:
            random.shuffle(sorted_players)

            match_counter = 1  # Initialize match_counter to 1
            for i in range(0, len(sorted_players), 2):
                match_id = f"{selected_event.event_name} - Round {round_number} - M{match_counter:02d}"
                player1 = sorted_players[i]
                player2 = sorted_players[i + 1] if i + 1 < len(
                    sorted_players) else None  # Handles odd number of players
                match = Match(match_id, player1, player2)
                matches.append(match)

                player1.opponents.append(player2)
                player2.opponents.append(player1)

                player1_info = f"{player1.chess_id} {player1.first_name} {player1.last_name}"
                player2_info = f"{player2.chess_id} {player2.first_name} {player2.last_name}" \
                    if player2 else "No opponent"
                match_counter += 1  # Increment by 1 to generate both even and odd match IDs
                selected_event.event_round_list[round_number - 1].matches.append(match)
                # Display match details before prompting the user to select the winner
                print(f"{match_id}", f"{player1_info}", f"{player2_info}", sep='\n')

                # Prompt the user to select the winner (1 for player 1, 2 for player 2, 3 for a draw)
                winner_input = input(
                    f"Select the winner (1 for {match.player1.chess_id} {match.player1.first_name}, "
                    f"2 for {match.player2.chess_id} {match.player2.first_name},"
                    f" 3 for a draw): "
                    "Or (9 to return, 0 to exit the application) : "
                )
                if winner_input == "1":
                    match.result = f"1-0"
                    match.player1.score += 1
                elif winner_input == "2":
                    match.result = f"0-1"
                    match.player2.score += 1
                elif winner_input == "3":
                    match.result = f"0.5-0.5"
                    match.player1.score += 0.5
                    match.player2.score += 0.5
                elif winner_input == "9":
                    break
                elif winner_input == "0":
                    exit()
                else:
                    print("Invalid input. Please enter 1, 2, or 3 to select the winner.")
                    # You can add error handling or prompt again if the input is invalid.
        elif round_number > 1:

            # Find the last match number and increment by 1
            match_counter = 1
            for i in range(0, len(sorted_players), 2):
                match_id = f"{selected_event.event_name} - Round {round_number} - M{match_counter:02d}"
                player1 = sorted_players[i]
                player2 = None  # Initialize player2 to None
                for j in range(i + 1, len(sorted_players), 2):  # Use a different variable (e.g., j) for the inner loop
                    if player2 is None and sorted_players[j] not in player1.opponents:
                        player2 = sorted_players[j]
                        break  # Exit the inner loop once player2 is found
                if player2 is None:
                    continue
                # Handles odd number of players
                match = Match(match_id, player1, player2)
                matches.append(match)

                player1.opponents.append(player2)
                player2.opponents.append(player1)

                player1_info = f"{player1.chess_id} {player1.first_name} {player1.last_name}"
                player2_info = f"{player2.chess_id} {player2.first_name} {player2.last_name}" \
                    if player2 else "No opponent"
                match_counter += 1  # Increment by 1 to generate both even and odd match IDs
                selected_event.event_round_list[round_number - 1].matches.append(match)
                # Display match details before prompting the user to select the winner
                print(f"{match_id}", f"{player1_info}", f"{player2_info}", sep='\n')

                # Prompt the user to select the winner (1 for player 1, 2 for player 2, 3 for a draw)
                winner_input = input(
                    f"Select the winner (1 for {match.player1.chess_id} {match.player1.first_name}, "
                    f"2 for {match.player2.chess_id} {match.player2.first_name},"
                    f" 3 for a draw): "
                    "Or (9 to return, 0 to exit the application) : "
                )
                if winner_input == "1":
                    match.result = f"1-0"
                    match.player1.score += 1
                elif winner_input == "2":
                    match.result = f"0-1"
                    match.player2.score += 1
                elif winner_input == "3":
                    match.result = f"0.5-0.5"
                    match.player1.score += 0.5
                    match.player2.score += 0.5
                elif winner_input == "9":
                    break
                elif winner_input == "0":
                    exit()
                else:
                    print("Invalid input. Please enter 1, 2, or 3 to select the winner.")
                    # You can add error handling or prompt again if the input is invalid.

        # Now, print the generated matches with results
        for match in matches:
            print(f"Match ID: {match.match_id}")
            print(f"Player 1: {match.player1.first_name} {match.player1.last_name}")
            if match.player2:
                print(f"Player 2: {match.player2.first_name} {match.player2.last_name}")
            else:
                print("Player 2: Bye")  # Handle cases where there's no opponent
            print(f"Match Result: {match.result}")
        return matches
