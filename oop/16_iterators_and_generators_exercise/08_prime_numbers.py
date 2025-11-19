def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    else:
        prime = True  # Flag variable
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
        return prime

def get_primes(input_list: list[int]):
    for num in input_list:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
