class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a+") as f:
            result = self.func(*args, **kwargs)
            f.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(8, 12)
mult(90, 9)
