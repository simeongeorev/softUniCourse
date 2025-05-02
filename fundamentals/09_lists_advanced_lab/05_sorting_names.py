names = input().split(", ")
sorted_names = list(sorted(names, key=lambda name: (-len(name), name)))
print(sorted_names)