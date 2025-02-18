n = float(input())

if n == 0:
    print("zero")
elif n > 0:
    if n < 1:
        print("small positive")
    elif n <= 1_000_000:
        print("positive")
    else:
        print("large positive")
elif n < 0:
    if n > -1:
        print("small negative")
    elif n >= -1_000_000:
        print("negative")
    else:
        print("large negative")
