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
                while True:
                    winner_input = input(
                        f"Select the winner (1 for {match.player1.chess_id} {match.player1.first_name}, "
                        f"2 for {match.player2.chess_id} {match.player2.first_name},"
                        f" 3 for a draw): "
                        "Or (0 to exit the application) : "
                    )
                    if winner_input == "1":
                        match.result = "1-0"
                        match.player1.score += 1
                        break  # Exit the loop if a valid input is provided
                    elif winner_input == "2":
                        match.result = "0-1"
                        match.player2.score += 1
                        break  # Exit the loop if a valid input is provided
                    elif winner_input == "3":
                        match.result = "0.5-0.5"
                        match.player1.score += 0.5
                        match.player2.score += 0.5
                        break  # Exit the loop if a valid input is provided
                    elif winner_input == "0":
                        exit()  # Exit the application if the user wants to exit
                    else:
                        print("Invalid input. Please enter 1, 2, or 3 to select the winner.")
                        # The loop will continue to ask for input until a valid option is provided
        elif round_number > 1:
            players_left = sorted_players.copy()
            match_counter = 1

            while len(players_left) >= 2:
                match_id = f"{selected_event.event_name} - Round {round_number} - M{match_counter:02d}"
                player1 = players_left.pop(0)
                player2 = None
                for opponent_candidate in players_left:
                    if opponent_candidate not in player1.opponents:
                        player2 = opponent_candidate
                        players_left.remove(opponent_candidate)
                        break

                if player1 is not None and player2 is not None:
                    match = Match(match_id, player1, player2)
                    player1.opponents.append(player2)
                    player2.opponents.append(player1)
                    matches.append(match)

                    player1_info = f"{player1.chess_id} {player1.first_name} {player1.last_name}"
                    player2_info = f"{player2.chess_id} {player2.first_name} {player2.last_name}"
                    selected_event.event_round_list[round_number - 1].matches.append(match)

                    while True:
                        print(f"{match_id}", f"{player1_info}", f"{player2_info}", sep='\n')
                        winner_input = input(
                            f"Select the winner (1 for {player1.chess_id} {player1.first_name}, "
                            f"2 for {player2.chess_id} {player2.first_name},"
                            f" 3 for a draw): "
                            "Or (0 to exit the application) : "
                        )
                        if winner_input == "1":
                            match.result = "1-0"
                            player1.score += 1
                            player2.score += 0
                            break
                        elif winner_input == "2":
                            match.result = "0-1"
                            player1.score += 0
                            player2.score += 1
                            break
                        elif winner_input == "3":
                            match.result = "0.5-0.5"
                            player1.score += 0.5
                            player2.score += 0.5
                            break
                        elif winner_input == "0":
                            exit()  # Exit the application if the user wants to exit
                        else:
                            print("Invalid input. Please enter 1, 2, or 3 to select the winner.")
                    match_counter += 1

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
