command = input()

primes_sum = 0
non_primes_sum = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True

    if 2 > number >= 0:
        is_prime = False
    else:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False

    if is_prime:
        primes_sum += number
    else:
        non_primes_sum += number

    command = input()
else:
    print(f"Sum of all prime numbers is: {primes_sum}")
    print(f"Sum of all non prime numbers is: {non_primes_sum}")