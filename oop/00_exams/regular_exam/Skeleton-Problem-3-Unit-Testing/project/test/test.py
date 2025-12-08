from project.star_system import StarSystem
from unittest import TestCase, main


class StarSystemTest(TestCase):
    def setUp(self):
        self.star_system = StarSystem("Test Name", 'Red giant',
                                      'Single', 2, (1, 3))

    def test_init(self):
        self.assertEqual("Test Name", self.star_system.name)
        self.assertEqual('Red giant', self.star_system.star_type)
        self.assertEqual('Single', self.star_system.system_type)
        self.assertEqual(2, self.star_system.num_planets)
        self.assertEqual((1, 3), self.star_system.habitable_zone_range)

    def test_class_vars(self):
        self.assertEqual({'Red giant', 'Blue giant', 'Yellow dwarf', 'Red dwarf', 'Brown dwarf'},
                         StarSystem._STAR_TYPES)
        self.assertEqual({'Single', 'Binary', 'Triple', 'Multiple'}, StarSystem._STAR_SYSTEM_TYPES)

    def test_init_default(self):
        s_s = StarSystem("Test Name", 'Red giant', 'Single', 2)
        self.assertIsNone(s_s.habitable_zone_range)

    def test_is_habitable(self):
        self.assertTrue(self.star_system.is_habitable)  # true

        self.star_system.habitable_zone_range = None
        self.assertFalse(self.star_system.is_habitable)  # false and true

        self.star_system.num_planets = 0
        self.assertFalse(self.star_system.is_habitable)  # false and false

        self.star_system.habitable_zone_range = (1, 3)
        self.assertFalse(self.star_system.is_habitable)  # true and false

    def test_name_setter_raises(self):
        exp = "Name must be a non-empty string."

        with self.assertRaises(ValueError) as ex:
            self.star_system.name = " "
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.star_system.name = ""
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual("Test Name", self.star_system.name)

    def test_name_setter(self):
        self.star_system.name = "Changed"
        self.assertEqual("Changed", self.star_system.name)

    def test_star_type_setter_raises(self):
        exp = ("Star type must be one of "
               "['Blue giant', 'Brown dwarf', 'Red dwarf', 'Red giant', 'Yellow dwarf'].")

        with self.assertRaises(ValueError) as ex:
            self.star_system.star_type = "test"
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual('Red giant', self.star_system.star_type)

    def test_star_type_setter(self):
        self.star_system.star_type = 'Yellow dwarf'
        self.assertEqual('Yellow dwarf', self.star_system.star_type)

    def test_system_type_setter_raises(self):
        exp = "System type must be one of ['Binary', 'Multiple', 'Single', 'Triple']."

        with self.assertRaises(ValueError) as ex:
            self.star_system.system_type = "test"
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual('Single', self.star_system.system_type)

    def test_system_type_setter(self):
        self.star_system.system_type = 'Multiple'
        self.assertEqual('Multiple', self.star_system.system_type)

    def test_num_planets_setter_raises(self):
        exp = "Number of planets must be a non-negative integer."

        with self.assertRaises(ValueError) as ex:
            self.star_system.num_planets = -1
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual(2, self.star_system.num_planets)

    def test_num_planets_setter(self):
        self.star_system.num_planets = 1
        self.assertEqual(1, self.star_system.num_planets)

    def test_habitable_zone_range_setter_raises(self):
        exp = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1,)
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1, 2, 3)
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (1, 1)
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.star_system.habitable_zone_range = (3, 1)
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual((1, 3), self.star_system.habitable_zone_range)

    def test_habitable_zone_range_setter(self):
        self.star_system.habitable_zone_range = None
        self.assertEqual(None, self.star_system.habitable_zone_range)

        self.star_system.habitable_zone_range = (3, 10)
        self.assertEqual((3, 10), self.star_system.habitable_zone_range)

    def test_gt_raises(self):
        other = StarSystem("Test Name", 'Red giant',
                           'Single', 2)

        exp = "Comparison not possible: One or both systems lack a defined habitable zone or planets."

        with self.assertRaises(ValueError) as ex:
            bul = self.star_system > other
        self.assertEqual(exp, str(ex.exception))

        s_s = StarSystem("Test Name", 'Red giant',
                         'Single', 0, (1, 4))

        with self.assertRaises(ValueError) as ex:
            bul = s_s > self.star_system
        self.assertEqual(exp, str(ex.exception))

    def test_gt(self):
        # true
        s_s = StarSystem("Test Name", 'Red giant',
                         'Single', 2, (1, 4))
        self.assertTrue(s_s > self.star_system)

        # false
        self.assertFalse(self.star_system > s_s)

    def test_compare_star_systems(self):
        s_s = StarSystem("Test Name s_s", 'Red giant',
                         'Single', 2, (1, 4))
        exp = "Test Name s_s has a wider habitable zone than Test Name."
        self.assertEqual(exp, StarSystem.compare_star_systems(s_s, self.star_system))

        s_s.habitable_zone_range = (1,3)
        exp = "Test Name s_s has a wider or equal habitable zone compared to Test Name."
        self.assertEqual(exp, StarSystem.compare_star_systems(self.star_system, s_s))

        s_s.habitable_zone_range = (1, 2)
        exp = "Test Name has a wider or equal habitable zone compared to Test Name s_s."
        self.assertEqual(exp, StarSystem.compare_star_systems(s_s, self.star_system))

    def test_compare_star_systems_fails(self):
        s_s = StarSystem("Test Name s_s", 'Red giant',
                         'Single', 0, (1, 4))

        exp = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(exp, StarSystem.compare_star_systems(s_s, self.star_system))


if __name__ == '__main__':
    main()
