chars_list = input().split(", ")
chars_dict = {char:ord(char) for char in chars_list}

print(chars_dict)