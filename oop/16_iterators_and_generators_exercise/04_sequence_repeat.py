class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.idx = -1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1
        self.index += 1
        if self.index == len(self.sequence):
            self.index = 0
        if self.idx < self.number:
            return self.sequence[self.index]
        raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
