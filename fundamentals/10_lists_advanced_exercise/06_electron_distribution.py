electrons = int(input())

def electrons_in_a_shell(n: int):
    return 2 * n ** 2

filled_shells = []
counter = 1
electrons_left = electrons

while True:
    shell = electrons_in_a_shell(counter)
    electrons_left -= shell
    if electrons_left > 0:
        filled_shells.append(shell)

    else:
        filled_shells.append(electrons - sum(filled_shells))
        break
    counter += 1

print(filled_shells)
