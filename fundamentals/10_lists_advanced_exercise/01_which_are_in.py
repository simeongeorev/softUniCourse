first_strings = input().split(", ")
second_strings = input().split(", ")

new_strings = [word1 for word1 in first_strings if any(word1 in word2 for word2 in second_strings)]

print(new_strings)
