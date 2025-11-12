from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food) -> str | None:
        if type(food).__name__ not in ["Vegetable", "Fruit"]:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity
        return None


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food) -> str | None:
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity
        return None


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food) -> str | None:
        if type(food).__name__ not in ["Meat", "Vegetable"]:
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity
        return None

class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food) -> str | None:
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
        return None
