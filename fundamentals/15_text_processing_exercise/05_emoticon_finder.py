text = list(input())
emojis = []

for i in range(len(text)):
    if text[i] == ":" and text[i+1] != " ":
        emojis.append("".join(text[i:i+2]))

for em in emojis:
    print(em)
