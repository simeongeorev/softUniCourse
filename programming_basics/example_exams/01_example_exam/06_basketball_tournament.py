name_of_tournament = input()
team_1_score = 0
team_2_score = 0
matches_played_counter = 0
matches_won_counter = 0
matches_lost_counter = 0

while name_of_tournament != "End of tournaments": # tournament

    number_of_matches_played = int(input())

    for match_number in range(1, number_of_matches_played + 1): # match ex - 3

        matches_played_counter += 1

        our_team_score = int(input())
        their_team_score = int(input())

        if our_team_score > their_team_score: # winners
            print(f"Game {match_number} of tournament {name_of_tournament}:"
                  f" win with {our_team_score - their_team_score} points.")
            matches_won_counter += 1
        else: # losers
            print(f"Game {match_number} of tournament {name_of_tournament}:"
                  f" lost with {their_team_score - our_team_score} points.")
            matches_lost_counter += 1

    name_of_tournament = input()

else:
    print(f"{matches_won_counter / matches_played_counter * 100:.2f}% matches win")
    print(f"{matches_lost_counter / matches_played_counter * 100:.2f}% matches lost")