numbers_list = input().split()
n = int(input())

# making the strings into ints
for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])

sorted_list = list(numbers_list)
sorted_list.sort()

del sorted_list[n:]

for i in range(len(sorted_list)):
    numbers_list.remove(sorted_list[i])

for i in range(len(numbers_list)):
    numbers_list[i] = str(numbers_list[i])

print(", ".join(numbers_list))