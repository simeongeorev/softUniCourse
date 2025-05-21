distances = list(map(int, input().split()))

deleted_elements = []

while True:
    index = int(input())

    index_state = ""

    if index < 0:
        index = 0
        index_state = "lower"

    if index > len(distances) - 1:
        index = len(distances) - 1
        index_state = "higher"

    chosen_number = distances[index]
    deleted_elements.append(chosen_number)

    del distances[index]

    new_distances = [(distance + chosen_number)
                     if distance <= chosen_number
                     else (distance - chosen_number)
                     for distance in distances]

    distances = new_distances

    if index_state == "lower":
        distances.insert(0, distances[-1])

    if index_state == "higher":
        distances.append(distances[0])

    if len(distances) == 0:
        break

print(sum(deleted_elements))
