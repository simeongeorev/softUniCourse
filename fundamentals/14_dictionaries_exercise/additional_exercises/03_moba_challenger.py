player_position_dict = {}
ARROW = " -> "
VS = " vs "
while True:
    command = input()
    if command == "Season end":
        break

    if ARROW in command:
        command_list = command.split(ARROW)
        player, position, skill = command_list[0], command_list[1], int(command_list[2])
        if player not in player_position_dict.keys():
            player_position_dict[player] = {}

        if position not in player_position_dict[player].keys():
            player_position_dict[player][position] = 0

        if skill > player_position_dict[player][position]:
            player_position_dict[player][position] = skill

    elif VS in command:
        command_list = command.split(VS)
        player1, player2 = command_list
        position_to_duel = ""
        if player1 in player_position_dict.keys() and player2 in player_position_dict.keys():
            for position in player_position_dict[player1].keys():
                if position in player_position_dict[player2].keys():
                    position_to_duel = position

        if position_to_duel == "":
            continue

        player1_total_points = 0
        for points in player_position_dict[player1].values():
            player1_total_points += points

        player2_total_points = 0
        for points in player_position_dict[player2].values():
            player2_total_points += points

        if player1_total_points > player2_total_points:
            del player_position_dict[player2]
        elif player2_total_points > player1_total_points:
            del player_position_dict[player1]

# strongest_player = ""
# most_points = 0
# for player, position in player_position_dict.items():
#     if sum(position.values()) > most_points:
#         strongest_player = player
#         most_points = sum(position.values())

player_total_points_dict = {}
for player, position in player_position_dict.items():
    player_total_points_dict[player] = sum(position.values())
sorted_player_total_points_dict = dict(sorted(player_total_points_dict.items(), key=lambda item:item[1], reverse=True))
for player, total_points in sorted_player_total_points_dict.items():
    print(f"{player}: {total_points} skill")

# TODO figure out the sorting