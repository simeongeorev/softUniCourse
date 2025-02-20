budget = float(input())
flour_price_per_kilo = float(input())

eggs_price_per_package = flour_price_per_kilo * 0.75

milk_price_per_litre = flour_price_per_kilo * 1.25
milk_for_a_bread = milk_price_per_litre / 4

price_for_one_bread = flour_price_per_kilo + eggs_price_per_package + milk_for_a_bread

breads_total = int(budget // price_for_one_bread)

price_for_all_breads = breads_total * price_for_one_bread

colored_eggs = 0

for current_bread_count in range(1, breads_total + 1):
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

print(f"You made {breads_total} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {budget - price_for_all_breads:.2f}BGN left.")
