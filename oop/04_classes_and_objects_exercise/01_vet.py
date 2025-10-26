class Vet:
    animals = [] # all animals for all vets
    space = 5 # capacity if the clinic

    def __init__(self, name: str):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name: str) -> str:
        if self.get_space_left_in_clinic() > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return (f"{self.name} has {len(self.animals)} animals."
                f" {self.get_space_left_in_clinic()} space left in clinic")

    def get_space_left_in_clinic(self) -> int:
        return self.space - len(Vet.animals)


# vet = Vet("Bob")
# Vet.animals = []
# Vet.space = 5
# print(vet.register_animal("Kitty"))
# print(vet.unregister_animal("Kitty"))

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())


# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_init(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         self.assertEqual(vet.name, "Bob")
#         self.assertEqual(vet.animals, [])
#         self.assertEqual(Vet.animals, [])
#         self.assertEqual(Vet.space, 5)
#
#     def test_register_successfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         vet2 = Vet("Peter")
#         res = vet.register_animal("Doggy")
#         self.assertEqual(res, "Doggy registered in the clinic")
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet.animals, ["Doggy"])
#         self.assertEqual(vet2.animals, [])
#
#     def test_register_unsuccessfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         for i in range(6):
#             vet.register_animal(str(i))
#         res = vet.register_animal("Doggy")
#         self.assertEqual(res, "Not enough space")
#         self.assertEqual(len(Vet.animals), 5)
#         self.assertEqual(len(vet.animals), 5)
#
#     def test_unregister_successfull(self):
#         vet = Vet("Bob")
#         Vet.animals = []
#         Vet.space = 5
#         vet.register_animal("Kitty")
#         res = vet.unregister_animal("Kitty")
#         self.assertEqual(res, "Kitty unregistered successfully")
#         self.assertEqual(vet.animals, [])
#         self.assertEqual(Vet.animals, [])
#
#
# if __name__ == "__main__":
#     unittest.main()