from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food) -> str | None:
        if type(food).__name__ != "Meat":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"

        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity
        return None

class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

