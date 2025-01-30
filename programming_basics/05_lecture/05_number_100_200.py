#    • под 100 отпечатайте: "Less than 100"
#    • между 100 и 200 отпечатайте: "Between 100 and 200"
#    • над 200 отпечатайте: "Greater than 200"

number = int(input())

if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
