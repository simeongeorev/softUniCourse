nylon = int(input())
paint = int(input())
razreditel = int(input())
hours_to_finish_the_work = int(input())

nylon_sum = (nylon + 2) * 1.50
paint_sum = (paint * 1.1) * 14.50
razreditel_sum = razreditel * 5.00
bags = 0.40

materials_sum = nylon_sum + paint_sum + razreditel_sum + bags
worker_sum = (materials_sum * 0.30) * hours_to_finish_the_work

total = materials_sum + worker_sum

print(total)

