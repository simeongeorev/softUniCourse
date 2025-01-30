#Годишната такса за тренировки по баскетбол –
# цяло число в интервала [0… 9999]
#    • Баскетболни кецове – цената им е 40% по-малка от таксата за една година
#    • Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
#    • Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
#   • Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

annual_basketball_price = int(input())

shoes = annual_basketball_price * 0.6
suit = shoes * 0.8
ball = suit * 0.25
accessories = ball * 0.2

whole_annual_price = annual_basketball_price + shoes + suit + ball + accessories

print(whole_annual_price)