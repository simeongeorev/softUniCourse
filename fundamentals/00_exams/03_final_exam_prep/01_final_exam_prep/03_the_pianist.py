n = int(input())

pieces_dict = {}

for _ in range(n):
    submission = input().split("|")
    pieces_dict[submission[0]] = [submission[1], submission[2]]

while (command := input()) != "Stop":
    command_list = command.split("|")
    command = command_list[0]
    piece = command_list[1]
    if command == "Add":
        composer = command_list[2]
        key = command_list[3]
        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if piece in pieces_dict.keys():
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = command_list[2]
        if piece in pieces_dict.keys():
            pieces_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for item in pieces_dict.items():
    print(f"{item[0]} -> Composer: {item[1][0]}, Key: {item[1][1]}")