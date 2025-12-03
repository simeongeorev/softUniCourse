from project.furniture import Furniture
from unittest import TestCase, main

class FurnitureTest(TestCase):
    def setUp(self):
        self.furniture = Furniture("Test string lorem ipsum",
                              10.99,
                              (10, 20, 30),
                              True,
                              9.9)

    def test_init_with_all_params(self):
        self.assertEqual("Test string lorem ipsum", self.furniture.model)
        self.assertEqual(10.99, self.furniture.price)
        self.assertEqual((10, 20, 30), self.furniture.dimensions)
        self.assertTrue(self.furniture.in_stock)
        self.assertEqual(9.9, self.furniture.weight)

    def test_init_with_default_params(self):
        fur = Furniture("Test string lorem ipsum",
                              10.99,
                              (10, 20, 30))
        self.assertTrue(fur.in_stock)
        self.assertEqual(None, fur.weight)

    def test_model_setter_raises(self):
        expected = "Model must be a non-empty string with a maximum length of 50 characters."
        with self.assertRaises(ValueError) as ex:
            self.furniture.model = " "
        self.assertEqual(expected, str(ex.exception))

        self.assertEqual("Test string lorem ipsum", self.furniture.model)

        with self.assertRaises(ValueError) as ex:
            self.furniture.model = " Test string lorem ipsum, Test string lorem ipsum, Test string lorem ipsum"
        self.assertEqual(expected, str(ex.exception))

        self.assertEqual("Test string lorem ipsum", self.furniture.model)

    def test_model_setter(self):
        self.furniture.model = "Test"
        self.assertEqual("Test", self.furniture.model)

    def test_price_setter_raises(self):
        expected = "Price must be a non-negative number."
        with self.assertRaises(ValueError) as ex:
            self.furniture.price = -0.1
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(10.99, self.furniture.price)

    def test_price_setter(self):
        self.furniture.price = 0.0
        self.assertEqual(0.0, self.furniture.price)

        self.furniture.price = 0.1
        self.assertEqual(0.1, self.furniture.price)

    def test_dimensions_setter_raises_tuple_size(self):
        expected = "Dimensions tuple must contain 3 integers."
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (10, 20)
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((10, 20, 30), self.furniture.dimensions)

    def test_dimensions_setter_raises_invalid_dimensions(self):
        expected = "Dimensions tuple must contain integers greater than zero."
        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (0, 20, 30)
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((10, 20, 30), self.furniture.dimensions)

        with self.assertRaises(ValueError) as ex:
            self.furniture.dimensions = (10, -1, 30)
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual((10, 20, 30), self.furniture.dimensions)

    def test_dimensions_setter(self):
        self.furniture.dimensions = (1, 2 ,3)
        self.assertEqual((1, 2, 3), self.furniture.dimensions)

    def test_weight_setter_raises(self):
        expected = "Weight must be greater than zero."
        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = 0
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(9.9, self.furniture.weight)

        with self.assertRaises(ValueError) as ex:
            self.furniture.weight = -0.1
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual(9.9, self.furniture.weight)

    def test_weight_setter(self):
        self.furniture.weight = None
        self.assertEqual(None, self.furniture.weight)

        self.furniture.weight = 0.1
        self.assertEqual(0.1, self.furniture.weight)

    def test_get_available_status(self):
        expected = (f"Model: Test string lorem ipsum is currently "
                f"in stock.")
        self.assertEqual(expected, self.furniture.get_available_status())

        self.furniture.in_stock = False

        expected = (f"Model: Test string lorem ipsum is currently "
                    f"unavailable.")
        self.assertEqual(expected, self.furniture.get_available_status())

    def test_get_specifications(self):
        expected = (f"Model: Test string lorem ipsum has the following dimensions: "
                f"10mm x 20mm x 30mm and weighs: 9.9")
        self.assertEqual(expected, self.furniture.get_specifications())

        self.furniture.weight = None

        expected = (f"Model: Test string lorem ipsum has the following dimensions: "
                    f"10mm x 20mm x 30mm and weighs: N/A")
        self.assertEqual(expected, self.furniture.get_specifications())

if __name__ == '__main__':
    main()
