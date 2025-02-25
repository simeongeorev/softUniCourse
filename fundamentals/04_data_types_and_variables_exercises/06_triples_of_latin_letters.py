N = int(input())

ASCII_START = 97
ASCII_END = ASCII_START + N

for first_letter in range(ASCII_START, ASCII_END):
    for second_letter in range(ASCII_START, ASCII_END):
        for third_letter in range(ASCII_START, ASCII_END):
            print(chr(first_letter) + chr(second_letter) + chr(third_letter))