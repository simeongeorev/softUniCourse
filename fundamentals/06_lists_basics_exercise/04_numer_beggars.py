numbers_list = input().split(", ")
count_of_beggars = int(input())
beggars_results = [0] * count_of_beggars

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

for i in range(0, count_of_beggars):
    for j in range(i, len(numbers_list), count_of_beggars):
        beggars_results[i] += numbers_list[j]

print(beggars_results)
