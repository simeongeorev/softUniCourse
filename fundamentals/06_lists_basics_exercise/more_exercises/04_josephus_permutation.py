list_input = input().split()
length = len(list_input)
k = int(input())
result_list = []
index = k-1
for _ in range(length):
    if index >= len(list_input):
        index = index % len(list_input)
    result_list.append(list_input[index])
    del list_input[index]
    index+=k-1

print("["+ ",".join(result_list) +"]")
