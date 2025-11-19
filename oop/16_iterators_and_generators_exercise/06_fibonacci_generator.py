def fibonacci():
    current_n = 0
    next_n = 1
    yield current_n
    yield next_n
    while True:
        current_n, next_n = next_n, current_n + next_n
        yield next_n


generator = fibonacci()
for i in range(10):
    print(next(generator))
print()
generator = fibonacci()
for i in range(1):
    print(next(generator))
