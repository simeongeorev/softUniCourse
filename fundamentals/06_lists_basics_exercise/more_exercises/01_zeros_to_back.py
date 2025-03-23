numbers_list = input().split(", ")

counter = 0

while True:
    if "0" in numbers_list:
        numbers_list.remove("0")
        counter += 1
    else:
        break

for i in range(counter):
    numbers_list.append("0")

print("[" + ", ".join(numbers_list) + "]")


