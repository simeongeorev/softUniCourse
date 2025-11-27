import unittest
from project.student import Student


class StudentTests(unittest.TestCase):

    def setUp(self):
        self.student = Student("Joro", {"Cooking": ["kak da gotvim", "kak da qdem"],
                    "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"]})

    def test_initialization_with_courses(self):
        self.assertEqual(self.student.name, "Joro")
        self.assertEqual(self.student.courses, {"Cooking": ["kak da gotvim", "kak da qdem"],
                    "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"]})

    def test_initialization_without_courses(self):
        student_name = "Georgi"
        student = Student(student_name)

        self.assertEqual(student.name, student_name)
        self.assertEqual(student.courses, {})

    # test enroll with already existing course name return message
    def test_enroll_with_existing_course_name(self):
        # return message test
        self.assertEqual(
            self.student.enroll("Cooking", ["musaka", "salata"]),
            "Course already added. Notes have been updated.")

        # state test
        self.assertEqual(
            self.student.courses, {"Cooking": ["kak da gotvim", "kak da qdem", "musaka", "salata"],
                                   "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"]})

    # course name different - adds new course name and new notes - return message + state change
    def test_enroll_with_new_course_and_notes(self):
        self.assertEqual(
            self.student.enroll("Rabota", ["kopane"], "Y"),
            "Course and course notes have been added.")

        self.assertEqual(
            self.student.courses,
            {"Cooking": ["kak da gotvim", "kak da qdem"],
             "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"],
             "Rabota": ["kopane"]}
        )

    def test_enroll_with_new_course_and_notes_default_flag(self):
        result = self.student.enroll("Rabota", ["kopane"])
        self.assertEqual(result, "Course and course notes have been added.")

        self.assertEqual(
            self.student.courses,
            {"Cooking": ["kak da gotvim", "kak da qdem"],
             "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"],
             "Rabota": ["kopane"]}
        )

    # course name different - adds new course name and new notes,
    # but the flag is false - return message + change state
    def test_enrol_with_new_course_and_new_notes_but_add_course_notes_false(self):
        self.assertEqual(
            self.student.enroll("Rabota", ["kopane"], "N"),
            "Course has been added.")

        self.assertEqual(
            self.student.courses,
            {"Cooking": ["kak da gotvim", "kak da qdem"],
             "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"],
             "Rabota": []}
        )

    # add notes - course name exists - return message + update state
    def test_add_notes_for_existing_course(self):
        self.assertEqual(
            self.student.add_notes("Cooking", "musaka"), "Notes have been updated")

        self.assertEqual(
            self.student.courses, {"Cooking": ["kak da gotvim", "kak da qdem", "musaka"],
                                   "Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"]})

    # add notes - course name doesn't exist - return message
    def test_add_notes_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Fishing", "musaka")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    # leave course - existing course name - return message and updated state
    def test_leave_course(self):
        self.assertEqual(self.student.leave_course("Cooking"), "Course has been removed")

        self.assertEqual(self.student.courses, {"Cleaning": ["kak da chistim", "kak da ne chistim", "kak da capame"]})

    # leave course - not existing name - return message and state unchanged
    def test_leave_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Fishing")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == "__main__":
    unittest.main()
