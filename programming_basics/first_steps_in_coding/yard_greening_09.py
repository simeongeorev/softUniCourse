# 7.61 per meter
# 18% discount

square_meters = float(input())

price_without_discount = square_meters * 7.61
discount = price_without_discount * 0.18
price_with_discount = price_without_discount - discount

print(f"The final price is: {price_with_discount} lv.")
print(f"The discount is: {discount} lv.")
