maiden_party_price = float(input())
love_wishes = int(input())
roses = int(input())
keychains = int(input())
caricatures = int(input())
lucky_surprises = int(input())

love_wishes_price = love_wishes * 0.6
roses_price = roses * 7.2
keychains_price = keychains * 3.6
caricatures_price = caricatures * 18.2
lucky_surprises_price = lucky_surprises * 22

total_sum = love_wishes_price + roses_price + keychains_price + caricatures_price + lucky_surprises_price

ordered_things_count = love_wishes + roses + keychains + caricatures + lucky_surprises

if ordered_things_count >= 25:
    total_sum *= 0.65

total_sum *= 0.9

if total_sum < maiden_party_price:
    print(f"Not enough money! {maiden_party_price - total_sum:.2f} lv needed.")
else:
    print(f"Yes! {total_sum - maiden_party_price:.2f} lv left.")