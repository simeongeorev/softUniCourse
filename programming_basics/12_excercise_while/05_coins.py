change = float(input())
two_levs = 2
one_lev = 1
fifty_st = 0.50
twenty_st = 0.20
ten_st = 0.10
five_st = 0.050
two_st = 0.020
one_st = 0.010

coins_used = 0

# while change != 0:
while round(change - two_levs, 2) >= 0:
    change -= two_levs
    coins_used += 1
while round(change - one_lev, 2) >= 0:
    change -= one_lev
    coins_used += 1
while round(change - fifty_st, 2) >= 0:
    change -= fifty_st
    coins_used += 1
while round(change - twenty_st, 2) >= 0:
    change -= twenty_st
    coins_used += 1
while round(change - ten_st, 2) >= 0:
    change -= ten_st
    coins_used += 1
while round(change - five_st, 2) >= 0:
    change -= five_st
    coins_used += 1
while round(change - two_st, 2) >= 0:
    change -= two_st
    coins_used += 1
while round(change - one_st, 2) >= 0:
    change -= one_st
    coins_used += 1

print(coins_used)
