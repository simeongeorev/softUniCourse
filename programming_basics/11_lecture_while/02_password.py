username = str(input())
password = str(input())

pass_attempt = str(input())

while True:
    if pass_attempt == password:
        print(f"Welcome {username}!")
        break
    else:
        pass_attempt = str(input())
