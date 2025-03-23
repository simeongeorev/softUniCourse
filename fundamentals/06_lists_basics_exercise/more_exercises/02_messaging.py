numbers_list = input().split()
word_list = list(input())
secret_word = ""

for num_sequence in numbers_list:
    if not word_list:
        break

    index = 0
    for num in num_sequence:
        index += int(num)

    if index > len(word_list):
        index = index % len(word_list)

    secret_word += word_list[index]
    del word_list[index]

    if not word_list:
        break

print(secret_word)

#TODO strange runtime error on the last check