import re

n = int(input())

for i in range(n):
    text = input()
    pattern_validator = r"^[@][#]+[A-Z][a-zA-Z0-9]{4,}[A-Z][@][#]+$"
    validation_match = re.match(pattern_validator, text)

    if validation_match:
        matched_text = validation_match.group()
        pattern_nums = r"\d"
        numbers_matches = re.findall(pattern_nums, matched_text)
        if numbers_matches:
            product_group = "".join(numbers_matches)
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
        continue