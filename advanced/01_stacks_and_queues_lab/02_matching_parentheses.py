text = input()
opening_parenth = []

for i in range(len(text)):
    if text[i] == "(":
        opening_parenth.append(i)
    elif text[i] == ")":
        print(text[opening_parenth.pop():i+1])