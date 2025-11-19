class dictionary_iter:

    def __init__(self, dict_item: dict):
        self.dict_item = dict_item
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        my_tuple = tuple(self.dict_item.items())
        self.index += 1
        if self.index < len(my_tuple):
            return my_tuple[self.index]
        raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
