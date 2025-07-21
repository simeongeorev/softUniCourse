text_list = list(input())
chars_to_del = 0

for i in range(len(text_list)):

    if text_list[i] == ">":
        chars_to_del += int(text_list[i+1])
        continue

    if chars_to_del > 0:
        text_list[i] = "."
        chars_to_del -= 1

text_list = [char for char in text_list if char != "."]
print("".join(text_list))