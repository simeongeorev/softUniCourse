from project.senior_student import SeniorStudent
from unittest import TestCase, main

class SeniorStudentTest(TestCase):
    def setUp(self):
        self.ss = SeniorStudent("0001", "Test", 2.0)

    def test_init(self):
        self.assertEqual("0001", self.ss.student_id)
        self.assertEqual("Test", self.ss.name)
        self.assertEqual(2.0, self.ss.student_gpa)
        self.assertIsInstance(self.ss.colleges, set)
        self.assertEqual(0, len(self.ss.colleges))

    def test_student_id_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.ss.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!",
                         str(ex.exception))

        self.assertEqual("0001", self.ss.student_id)

    def test_student_id_setter(self):
        self.ss.student_id = "0002"
        self.assertEqual("0002", self.ss.student_id)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.ss.name = "    "
        self.assertEqual("Student name cannot be null or empty!",
                         str(ex.exception))
        self.assertEqual("Test", self.ss.name)

        with self.assertRaises(ValueError) as ex:
            self.ss.name = ""
        self.assertEqual("Student name cannot be null or empty!",
                         str(ex.exception))
        self.assertEqual("Test", self.ss.name)

    def test_name_setter(self):
        self.ss.name = "NewTest"
        self.assertEqual("NewTest", self.ss.name)

    def test_student_gpa_setter_raises(self):
        # equal (=) to 1
        with self.assertRaises(ValueError) as ex:
            self.ss.student_gpa = 1
        self.assertEqual("Student GPA must be more than 1.0!",
                         str(ex.exception))
        self.assertEqual(2.0, self.ss.student_gpa)

        # lower (<) than 1
        with self.assertRaises(ValueError) as ex:
            self.ss.student_gpa = 0.9
        self.assertEqual("Student GPA must be more than 1.0!",
                         str(ex.exception))
        self.assertEqual(2.0, self.ss.student_gpa)

    def test_student_gpa_setter(self):
        self.ss.student_gpa = 1.1
        self.assertEqual(1.1, self.ss.student_gpa)

    def test_apply_to_college_fails(self):
        expected = 'Application failed!'
        actual = self.ss.apply_to_college(2.01,
                                          "Harvard")
        self.assertEqual(expected, actual)
        self.assertEqual(0, len(self.ss.colleges))

    def test_apply_to_college_success(self):
        expected = 'Test successfully applied to Harvard.'
        actual = self.ss.apply_to_college(1.99,
                                          "Harvard")
        self.assertEqual(expected, actual)

        self.assertIn("HARVARD", self.ss.colleges)
        self.assertEqual(1, len(self.ss.colleges))

    def test_update_gpa_fails(self):
        # equal (=) to 1
        expected = 'The GPA has not been changed!'
        actual = self.ss.update_gpa(1.0)
        self.assertEqual(expected, actual)
        self.assertEqual(2.0, self.ss.student_gpa)

        # lower (<) than 1
        actual = self.ss.update_gpa(0.99)
        self.assertEqual(expected, actual)
        self.assertEqual(2.0, self.ss.student_gpa)

    def test_update_gpa_success(self):
        expected = 'Student GPA was successfully updated.'
        actual = self.ss.update_gpa(2.1)
        self.assertEqual(expected, actual)
        self.assertEqual(2.1, self.ss.student_gpa)

    def test_eq_false(self):
        other_ss = SeniorStudent("0002",
                                 "OtherTest",
                                 1.9)
        self.assertFalse(self.ss == other_ss)

    def test_eq_true(self):
        other_ss = SeniorStudent("0002",
                                 "OtherTest",
                                 2.0)
        self.assertTrue(self.ss == other_ss)

if __name__ == '__main__':
    main()

