import re

text = input()

pattern = r"(?P<sym>[@|#])[a-zA-Z]{3,}(?P=sym)(?P=sym)[a-zA-Z]{3,}(?P=sym)"

matches = re.finditer(pattern, text)

matches_count = 0
mirrors_list = []

for match in matches:
    matches_count += 1
    whole_word = match.group()
    half_word_length = int(len(whole_word) / 2)
    str1 = whole_word[:half_word_length]
    str2 = whole_word[half_word_length:]

    if str2[::-1] == str1:
        mirrors_list.append(f"{str1[1:-1]} <=> {str2[1:-1]}")

if matches_count > 0:
    print(f"{matches_count} word pairs found!")
    if mirrors_list:
        print("The mirror words are:")
        print(", ".join(mirrors_list))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")
