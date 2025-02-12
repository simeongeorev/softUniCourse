# Един пакет захар е 950 грама, а един пакет брашно е 750 грама.
import math

n_kozunaci = int(input())

total_sugar_used = 0
total_flour_used = 0

max_sugar_used = 0
max_flour_used = 0

for _ in range(n_kozunaci):

    sugar_for_kozunak_grams = int(input())
    flour_for_kozunak_grams = int(input())

    total_sugar_used += sugar_for_kozunak_grams
    total_flour_used += flour_for_kozunak_grams

    if sugar_for_kozunak_grams > max_sugar_used:
        max_sugar_used = sugar_for_kozunak_grams

    if flour_for_kozunak_grams > max_flour_used:
        max_flour_used = flour_for_kozunak_grams

packets_of_sugar_needed = total_sugar_used / 950
packets_of_flour_needed = total_flour_used / 750

print(f"Sugar: {math.ceil(packets_of_sugar_needed)}\n"
             f"Flour: {math.ceil(packets_of_flour_needed)}\n"
             f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
