package_weight_kilos = float(input())
type_of_delivery = input()
distance_kms = int(input())

price_per_km_stotinki = 0
bonus_price_per_kilo = 0

if package_weight_kilos < 1:
    price_per_km_stotinki = 3
elif package_weight_kilos < 10:
    price_per_km_stotinki = 5
elif package_weight_kilos < 40:
    price_per_km_stotinki = 10
elif package_weight_kilos < 90:
    price_per_km_stotinki = 15
elif package_weight_kilos < 150:
    price_per_km_stotinki = 20

if type_of_delivery == "express":
    if package_weight_kilos < 1:
        bonus_price_per_kilo = package_weight_kilos * (0.8 * price_per_km_stotinki)
    elif package_weight_kilos < 10:
        bonus_price_per_kilo = package_weight_kilos * (0.4 * price_per_km_stotinki)
    elif package_weight_kilos < 40:
        bonus_price_per_kilo = package_weight_kilos * (0.05 * price_per_km_stotinki)
    elif package_weight_kilos < 90:
        bonus_price_per_kilo = package_weight_kilos * (0.02 * price_per_km_stotinki)
    elif package_weight_kilos < 150:
        bonus_price_per_kilo = package_weight_kilos * (0.01 * price_per_km_stotinki)

total_delivery_price_stotinki = distance_kms * price_per_km_stotinki + distance_kms * bonus_price_per_kilo
total_delivery_price_leva = total_delivery_price_stotinki / 100

print(f"The delivery of your shipment with weight of {package_weight_kilos:.3f} kg. would cost {total_delivery_price_leva:.2f} lv.")