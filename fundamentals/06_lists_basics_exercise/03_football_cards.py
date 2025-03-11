teams_score = input().split()
team_a_players = 11
team_b_players = 11
game_is_terminated = False

for i in range(0, len(teams_score)):
    if teams_score[i][0] == "A":
        team_a_players -= 1
    elif teams_score[i][0] == "B":
        team_b_players -= 1
    if team_a_players < 7 or team_b_players < 7:
        game_is_terminated = True
        break

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if game_is_terminated:
    print("Game was terminated")

# TODO not everything passes. Need to return to see why!