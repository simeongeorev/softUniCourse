from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name, age):
        super().__init__(name, age, gender="Female")

    @property
    def sound(self):
        return "Meow"
