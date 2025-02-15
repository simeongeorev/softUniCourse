a1 = int(input())
a2 = int(input())
n = int(input())

for i in range(a1, a2):
    symbol_1 = chr(i)
    for symbol_2 in range(1, n):
        for symbol_3 in range(1, int(n/2)):
            symbol_4 = i
            sum_of_symbols_2_to_4 = symbol_2 + symbol_3 + symbol_4
            if (i % 2 != 0) and (sum_of_symbols_2_to_4 % 2 != 0):
                print(f"{symbol_1}-{symbol_2}{symbol_3}{symbol_4}")