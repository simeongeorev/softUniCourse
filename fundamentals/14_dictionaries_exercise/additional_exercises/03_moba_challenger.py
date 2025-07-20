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

sorted_dict = dict(sorted(player_position_dict.items(),
                          key=lambda tup: (sum(tup[1].values())),
                          reverse=True))

for player, position_dict in sorted_dict.items():
    sorted_position_skill_dict = dict(sorted(position_dict.items(),
                                             key=lambda tup: tup[1],
                                             reverse=True))
    print(f"{player}: {sum(position_dict.values())} skill")
    for position, skill in sorted_position_skill_dict.items():
        print(f"- {position} <::> {skill}")

