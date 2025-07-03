iterations = int(input())

synonyms_dict = {}

for _ in range(iterations):
    key = input()
    value = input()

    if key not in synonyms_dict:
        synonyms_dict[key] = [value]
    else:
        synonyms_dict[key] += [value]

for key, value in synonyms_dict.items():
    print(f"{key} - {', '.join(value)}")
