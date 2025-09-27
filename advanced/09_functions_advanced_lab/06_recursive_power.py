def recursive_power(number, power):
    if power == 0:
        return 1
    return number * recursive_power(number, power - 1)

print(recursive_power(2, 3))

'''
recursive_power(2, 3)
= 2 * recursive_power(2, 2)
= 2 * (2 * recursive_power(2, 1))
= 2 * (2 * (2 * recursive_power(2, 0)))
= 2 * (2 * (2 * 1))
= 2 * (2 * 2)
= 2 * 4
= 8
'''