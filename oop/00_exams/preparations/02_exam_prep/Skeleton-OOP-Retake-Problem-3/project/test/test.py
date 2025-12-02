from project.gallery import Gallery
from unittest import TestCase, main


class GalleryTest(TestCase):
    def setUp(self):
        self.gallery = Gallery("TestGallery1", "Sofia", 10, open_to_public=True)

    def test_init(self):
        self.assertEqual("TestGallery1", self.gallery.gallery_name)
        self.assertEqual("Sofia", self.gallery.city)
        self.assertEqual(10, self.gallery.area_sq_m)
        self.assertTrue(self.gallery.open_to_public)
        self.assertIsInstance(self.gallery.exhibitions, dict)
        self.assertEqual(0, len(self.gallery.exhibitions))

    def test_open_to_public_init(self):
        g2 = Gallery("TestGallery1", "Sofia", 10, open_to_public=False)
        self.assertFalse(g2.open_to_public)

        g3 = Gallery("TestGallery1", "Sofia", 10)
        self.assertTrue(g3.open_to_public)

    def test_gallery_name_setter_raises(self):
        exp = "Gallery name can contain letters and digits only!"

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "Test.Gallery1"
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "Test Gallery1"
        self.assertEqual(exp, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.gallery_name = "./."
        self.assertEqual(exp, str(ex.exception))

        self.assertEqual("TestGallery1", self.gallery.gallery_name)

    def test_gallery_name_setter(self):
        self.gallery.gallery_name = "TestGalleryNew"
        self.assertEqual("TestGalleryNew", self.gallery.gallery_name)

    def test_city_setter_raises(self):
        exp_message = "City name must start with a letter!"

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = ""
        self.assertEqual(exp_message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = "1ofia"
        self.assertEqual(exp_message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = ".ofia"
        self.assertEqual(exp_message, str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.gallery.city = " Sofia"
        self.assertEqual(exp_message, str(ex.exception))

        self.assertEqual("Sofia", self.gallery.city)

    def test_city_setter(self):
        self.gallery.city = "Plovdiv"
        self.assertEqual("Plovdiv", self.gallery.city)

    def test_area_sq_m_setter_raises(self):
        exp_message = "Gallery area must be a positive number!"

        # equal to 0
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = 0.0
        self.assertEqual(exp_message, str(ex.exception))

        # lower than 0
        with self.assertRaises(ValueError) as ex:
            self.gallery.area_sq_m = -0.1
        self.assertEqual(exp_message, str(ex.exception))

        self.assertEqual(10, self.gallery.area_sq_m)

    def test_area_sq_m_setter(self):
        self.gallery.area_sq_m = 0.1
        self.assertEqual(0.1, self.gallery.area_sq_m)

    def test_add_exhibition(self):
        exp = 'Exhibition "TestEx" added for the year 2025.'
        act = self.gallery.add_exhibition("TestEx", 2025)
        self.assertEqual(exp, act)

        self.assertIn(("TestEx", 2025), self.gallery.exhibitions.items())
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_add_exhibition_fails(self):
        self.gallery.add_exhibition("TestEx", 2025)

        exp = 'Exhibition "TestEx" already exists.'
        act = self.gallery.add_exhibition("TestEx", 2025)
        self.assertEqual(exp, act)

        self.assertIn(("TestEx", 2025), self.gallery.exhibitions.items())
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_remove_exhibition(self):
        self.gallery.add_exhibition("TestEx", 2025)

        exp = 'Exhibition "TestEx" removed.'
        act = self.gallery.remove_exhibition("TestEx")

        self.assertEqual(exp, act)
        self.assertEqual(0, len(self.gallery.exhibitions))

    def test_remove_exhibition_fails(self):
        self.gallery.add_exhibition("TestEx", 2025)

        exp = 'Exhibition "TestEX" not found.'
        act = self.gallery.remove_exhibition("TestEX")
        self.assertEqual(exp, act)

        self.assertIn(("TestEx", 2025), self.gallery.exhibitions.items())
        self.assertEqual(1, len(self.gallery.exhibitions))

    def test_list_exhibitions(self):
        self.gallery.add_exhibition("TestEx", 2025)

        # open to public
        exp = "TestEx: 2025"
        act = self.gallery.list_exhibitions()
        self.assertEqual(exp, act)

        # closed to public
        self.gallery.open_to_public = False
        exp = 'Gallery TestGallery1 is currently closed for public! Check for updates later on.'
        act = self.gallery.list_exhibitions()
        self.assertEqual(exp, act)


if __name__ == '__main__':
    main()
