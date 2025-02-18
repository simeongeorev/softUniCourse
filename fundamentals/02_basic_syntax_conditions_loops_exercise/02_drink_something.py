age = int(input())

if age < 15:
    drink = "toddy"
elif age < 19:
    drink = "coke"
elif age < 22:
    drink = "beer"
elif age > 21:
    drink = "whisky"
print("drink " + drink)