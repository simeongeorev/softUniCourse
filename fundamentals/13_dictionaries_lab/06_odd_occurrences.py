sequence = list(map(lambda x: str(x).lower(), input().split()))

my_dict = {}

for char in sequence:
    if char not in my_dict.keys():
        my_dict[char] = 1
    else:
        my_dict[char] += 1


for key, value in my_dict.items():
    if value % 2 != 0:
        print(key, end=" ")