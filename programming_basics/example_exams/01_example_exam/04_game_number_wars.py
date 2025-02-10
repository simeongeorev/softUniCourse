name_player_1 = input()
name_player_2 = input()
end_of_game = False
player_1_points = 0
player_2_points = 0
number_wars = False

while True:
    command = input()
    if command == "End of game":
        end_of_game = True
        break
    player_1_card = int(command)

    second_command = input()
    if second_command == "End of game":
        end_of_game = True
        break
    player_2_card = int(second_command)

    if player_1_card > player_2_card and not number_wars: # if player 1 is winning
        player_1_points += player_1_card - player_2_card
    elif player_2_card > player_1_card and not number_wars: # if player 2 is winning
        player_2_points += player_2_card - player_1_card

    if player_1_card == player_2_card: # if they have a draw
        number_wars = True
        continue

    if number_wars:
        print("Number wars!")
        if player_1_card > player_2_card:
            print(f"{name_player_1} is winner with {player_1_points} points")
        else:
            print(f"{name_player_2} is winner with {player_2_points} points")
        exit()

if end_of_game:
    print(f"{name_player_1} has {player_1_points} points")
    print(f"{name_player_2} has {player_2_points} points")
    exit()