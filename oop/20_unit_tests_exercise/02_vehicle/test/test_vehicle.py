import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.veh = Vehicle(13.4, 59.9)

    def test_initialization(self):
        self.assertEqual(self.veh.fuel, 13.4)
        self.assertEqual(self.veh.capacity, 13.4)
        self.assertEqual(self.veh.horse_power, 59.9)
        self.assertEqual(self.veh.fuel_consumption, 1.25)

    def test_drive(self):
        self.veh.drive(10)
        self.assertAlmostEqual(self.veh.fuel, 0.9)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.veh.drive(30)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel(self):
        self.veh.drive(10)
        self.veh.refuel(10)
        self.assertEqual(self.veh.fuel, 10.9)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.veh.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_as_str(self):
        expected_result = f"The vehicle has {59.9} " \
               f"horse power with {13.4} fuel left and {1.25} fuel consumption"
        self.assertEqual(self.veh.__str__(), expected_result)

if __name__ == "__main__":
 unittest.main()