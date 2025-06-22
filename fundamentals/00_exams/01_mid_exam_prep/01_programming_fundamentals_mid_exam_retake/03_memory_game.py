elements_sequence = input().split()
moves = 0

while True:

    command = input()

    if command == "end":
        print("Sorry you lose :(")
        for element in elements_sequence:
            print(element, end=" ")
        break

    moves += 1

    indexes = list(map(int, command.split()))

    index_1 = indexes[0]
    index_2 = indexes[1]

    elements_sequence_range = range(len(elements_sequence))

    # invalid indexes
    if (index_1 == index_2
            or index_1 not in elements_sequence_range
            or index_2 not in elements_sequence_range):
        elements_sequence.insert(int(len(elements_sequence) / 2), f"-{moves}a")
        elements_sequence.insert(int(len(elements_sequence) / 2), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
        continue

    # correct guess
    if elements_sequence[index_1] == elements_sequence[index_2]:
        element = elements_sequence[index_1]
        elements_sequence.remove(element)
        elements_sequence.remove(element)
        print(f"Congrats! You have found matching elements - {element}!")

        # check if the list is empty and the player has won
        if len(elements_sequence) == 0:
            print(f"You have won in {moves} turns!")
            break
        else:
            continue

    # incorrect guess
    if elements_sequence[index_1] != elements_sequence[index_2]:
        print("Try again!")
        continue





