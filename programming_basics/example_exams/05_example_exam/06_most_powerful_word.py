import math

most_powerful_word_name = ""
most_powerful_word_points = 0

while True:
    word = input()

    if word == "End of words":
        break

    sum_of_ascii = 0

    for char in word:
        sum_of_ascii += ord(char)

    if word[0].lower() in "aeiouy":
        sum_of_ascii *= len(word)
    else:
        sum_of_ascii = math.floor(sum_of_ascii / len(word))

    if sum_of_ascii > most_powerful_word_points:
        most_powerful_word_points = sum_of_ascii
        most_powerful_word_name = word

print(f"The most powerful word is {most_powerful_word_name} - {most_powerful_word_points}")