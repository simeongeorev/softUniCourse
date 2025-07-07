text = input().replace(" ", "")

text_dict = {}

for char in text:
    if char not in text_dict.keys():
        text_dict[char] = 0
    text_dict[char] += 1

for char, count in text_dict.items():
    print(f"{char} -> {count}")