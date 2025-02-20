total_coffees = 0

while True:

    command = input()

    if command == "END":
        break

    if command in "codingdogcatmovie":
        total_coffees += 1
    elif command in "CODINGDOGCATMOVIE":
        total_coffees += 2
    else:
        continue

if total_coffees > 5:
    print("You need extra sleep")
else:
    print(total_coffees)

