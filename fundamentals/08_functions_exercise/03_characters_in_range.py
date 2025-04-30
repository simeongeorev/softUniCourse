def chars_in_range(char1: str, char2: str):
    ascii_positions = list(range(ord(char1) + 1, ord(char2)))
    chars_string = ""
    for position in ascii_positions:
        chars_string += chr(position) + " "
    return chars_string



print(str(chars_in_range(input(), input())))
