text = input()
new_text = ""

for i in range(len(text)-1):
    if text[i] == text[i+1]:
        continue
    new_text += text[i]
new_text += text[-1]
print(new_text)