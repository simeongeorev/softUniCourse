first_game = input()
second_game = input()
third_game = input()

wins = 0
losts = 0
draws = 0

our_team_result_first = int(first_game[0])
our_team_result_second = int(second_game[0])
our_team_result_third = int(third_game[0])

their_team_result_first = int(first_game[-1])
their_team_result_second = int(second_game[-1])
their_team_result_third = int(third_game[-1])

if our_team_result_first > their_team_result_first:
    wins += 1
elif our_team_result_first == their_team_result_first:
    draws += 1
else:
    losts += 1

if our_team_result_second > their_team_result_second:
    wins += 1
elif our_team_result_second == their_team_result_second:
    draws += 1
else:
    losts += 1

if our_team_result_third > their_team_result_third:
    wins += 1
elif our_team_result_third == their_team_result_third:
    draws += 1
else:
    losts += 1

print(f"Team won {wins} games.")
print(f"Team lost {losts} games.")
print(f"Drawn games: {draws}")