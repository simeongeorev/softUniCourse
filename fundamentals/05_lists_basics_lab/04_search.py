n = int(input())
key_word = input()

strings = []

for _ in range(n):
    input_string = input()
    strings.append(input_string)

print(strings)

for i in range(len(strings) - 1, -1, -1):
    if key_word not in strings[i]:
        strings.remove(strings[i])

print(strings)