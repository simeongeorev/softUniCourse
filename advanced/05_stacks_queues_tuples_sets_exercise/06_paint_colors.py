import math
from collections import deque

substrings = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
all_colors = main_colors + secondary_colors

all_colors_found = []
main_colors_found = []

while substrings:

    # final word check
    if len(substrings) == 1:
        final_word = substrings.popleft()
        if final_word in all_colors:
            all_colors_found.append(final_word)
            if final_word in main_colors:
                main_colors_found.append(final_word)
        break

    first_word = substrings[0]
    last_word = substrings[-1]

    # happy path
    if first_word + last_word in all_colors:
        valid_color = first_word + last_word
        all_colors_found.append(valid_color)
        if valid_color in main_colors:
            main_colors_found.append(valid_color)
        substrings.popleft()
        substrings.pop()
        continue

    elif last_word + first_word in all_colors:
        valid_color = last_word + first_word
        all_colors_found.append(valid_color)
        if valid_color in main_colors:
            main_colors_found.append(valid_color)
        substrings.popleft()
        substrings.pop()
        continue

    # edge case - not a valid color
    else:
        first_word = first_word[:-1]
        last_word = last_word[:-1]
        words_list = []
        if first_word:
            words_list.append(first_word)
        if last_word:
            words_list.append(last_word)

        substrings.popleft()
        substrings.pop()

        if len(substrings) % 2 == 0:
            half_length = int(len(substrings) / 2)
        else:
            half_length = math.ceil(len(substrings) / 2)
        substrings = deque(list(substrings)[:half_length]
                               + words_list
                               + list(substrings)[half_length:])

for color in all_colors_found:
    if color in secondary_colors:
        if color == "orange" and "red" in main_colors_found and "yellow" in main_colors_found:
            continue
        elif color == "purple" and "red" in main_colors_found and "blue" in main_colors_found:
            continue
        elif color == "green" and "yellow" in main_colors_found and "blue" in main_colors_found:
            continue
        all_colors_found.remove(color)

print(all_colors_found)

