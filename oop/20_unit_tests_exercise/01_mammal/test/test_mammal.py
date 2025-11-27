import unittest
from project.mammal import Mammal

class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Lion", "Carnivore", "Rawr")

    def test_initialization(self):
        self.assertEqual(self.mammal.name, "Lion")
        self.assertEqual(self.mammal.type, "Carnivore")
        self.assertEqual(self.mammal.sound, "Rawr")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        expected_result = "Lion makes Rawr"
        self.assertEqual(result, expected_result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected = "animals"
        self.assertEqual(result, expected)

    def test_info(self):
        result = self.mammal.info()
        expected = f"Lion is of type Carnivore"
        self.assertEqual(result, expected)

if __name__ == "__main__":
 unittest.main()