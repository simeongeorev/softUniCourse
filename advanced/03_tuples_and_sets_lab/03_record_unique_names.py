number_of_names = int(input())
names = set()
for _ in range(number_of_names):
    names.add(input())

print("\n".join(names))