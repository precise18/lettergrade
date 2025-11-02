import unittest
from letter import letter_grade

class TestLetterGrade(unittest.TestCase):

    def test_grade_A(self):
        self.assertEqual(letter_grade(80),"A")
    print("You passed with an A")

    def test_grade_B(self):
        self.assertEqual(letter_grade(70),"B")
    print("You passed with a B")

    def test_grade_C(self):
        self.assertEqual(letter_grade(60),"C")
    print("You passed with a C")

    def test_grade_D(self):
        self.assertEqual(letter_grade(50),"D")
    print("You passed with an D")

    def test_grade_D(self):
        self.assertEqual(letter_grade(40), "F")
    print("You got an F")

if __name__ == "__main__":
    unittest.main()