secret_words = input().split()
deciphered_message = []

for word in secret_words:
    number_str = ""
    rest_of_str = ""
    for char in word:
        if char.isnumeric():
            number_str += char
        else:
            rest_of_str += char
    secret_letter = chr(int(number_str))

    whole_word = secret_letter + rest_of_str

    word_list = list(whole_word)
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    revealed_word = "".join(word_list)
    deciphered_message.append(revealed_word)

print(" ".join(deciphered_message))
