strings = input().split()

str1, str2 = strings


def multiply_char_codes(str1: str, str2: str) -> int:
    total = 0
    for i in range((len(str1))):
        total += ord(str1[i]) * ord(str2[i])
    return total


if len(str1) > len(str2):
    total = multiply_char_codes(str2, str1)
    str_left = str1[len(str2):]
    for char in str_left:
        total += ord(char)
    print(total)
else:
    total = multiply_char_codes(str1, str2)
    str_left = str2[len(str1):]
    for char in str_left:
        total += ord(char)
    print(total)
