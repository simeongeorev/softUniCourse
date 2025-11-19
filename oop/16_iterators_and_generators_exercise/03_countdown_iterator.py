class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.index = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.index
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print()
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
