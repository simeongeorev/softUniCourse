path = input().split("\\")
name_and_extension = path[-1].split(".")
name, path = name_and_extension
print(f"File name: {name}")
print(f"File extension: {path}")
