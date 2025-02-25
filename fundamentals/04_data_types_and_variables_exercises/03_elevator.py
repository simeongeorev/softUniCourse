import math

persons = int(input())
capacity = int(input())

trips = math.ceil(persons / capacity)

print(trips)