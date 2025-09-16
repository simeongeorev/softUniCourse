n = int(input())
odd_set = set()
even_set = set()
for i in range(n):
    name = input()
    ascii_sum = 0

    for char in name:
        ascii_sum += ord(char)

    ready_sum = int(ascii_sum / (i+1))

    if ready_sum % 2 != 0:
        odd_set.add(ready_sum)
    else:
        even_set.add(ready_sum)

odd_sum = sum(odd_set)
even_sum = sum(even_set)

if odd_sum > even_sum:
    print(', '.join(str(num) for num in odd_set.difference(even_set)))
elif odd_sum < even_sum:
    print(', '.join(str(num) for num in even_set.symmetric_difference(odd_set)))
elif odd_sum == even_sum:
    print(', '.join(str(num) for num in odd_set.union(even_set)))