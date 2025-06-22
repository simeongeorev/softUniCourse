import math

budget = float(input())
students = int(input())
flour_package_price = float(input())
single_egg_price = float(input())
single_apron_price = float(input())

total_flour = (students * flour_package_price) - ((students // 5) * flour_package_price)
total_eggs = students * 10 * single_egg_price
total_apron = math.ceil(students * 1.2) * single_apron_price

total_price = total_flour + total_eggs + total_apron

if budget >= total_price:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")


