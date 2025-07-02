class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)

        elif species == "fish":
            self.fishes.append(name)

        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"

        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"

        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
my_zoo = Zoo(zoo_name)

entries = int(input())
for i in range(entries):
    add_animal_list = input().split()
    my_zoo.add_animal(add_animal_list[0], add_animal_list[1])

specie = input()
print(my_zoo.get_info(specie))
