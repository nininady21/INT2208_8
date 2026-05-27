import unittest
from loan import loan


class TestLoan(unittest.TestCase):

    # TC01 - Age < 18
    def test_TC01(self):
        self.assertEqual(loan(17, 20, 700, "C"), "Invalid Input")

    # TC02 - Age > 65
    def test_TC02(self):
        self.assertEqual(loan(66, 20, 700, "C"), "Invalid Input")

    # TC03 - Income < 5
    def test_TC03(self):
        self.assertEqual(loan(30, 4.9, 700, "C"), "Invalid Input")

    # TC04 - Income > 500
    def test_TC04(self):
        self.assertEqual(loan(30, 500.1, 700, "C"), "Invalid Input")

    # TC05 - Credit score < 300
    def test_TC05(self):
        self.assertEqual(loan(30, 20, 299, "C"), "Invalid Input")

    # TC06 - Credit score > 850
    def test_TC06(self):
        self.assertEqual(loan(30, 20, 851, "C"), "Invalid Input")

    # TC07 - Invalid employment type
    def test_TC07(self):
        self.assertEqual(loan(30, 20, 700, "X"), "Invalid Input")

    # TC08 - Invalid datatype
    def test_TC08(self):
        self.assertEqual(loan("30", 20, 700, "C"), "Invalid Input")

    # TC09 - Reject because credit score too low
    def test_TC09(self):
        self.assertEqual(loan(30, 20, 400, "C"), "REJECT")

    # TC10 - Reject because income too low
    def test_TC10(self):
        self.assertEqual(loan(30, 10, 600, "C"), "REJECT")

    # TC11 - Reject because freelance + low score
    def test_TC11(self):
        self.assertEqual(loan(30, 10, 750, "F"), "REJECT")

    # TC12 - Manual review
    def test_TC12(self):
        self.assertEqual(loan(30, 10, 750, "C"), "MANUAL REVIEW")

    # TC13 - Approve
    def test_TC13(self):
        self.assertEqual(loan(30, 20, 600, "C"), "APPROVE")

    # TC14 - Freelance manual review
    def test_TC14(self):
        self.assertEqual(loan(30, 20, 600, "F"), "MANUAL REVIEW")

    # TC15 - Approve with high score
    def test_TC15(self):
        self.assertEqual(loan(30, 20, 750, "C"), "APPROVE")

    # TC16 - Freelance high score manual review
    def test_TC16(self):
        self.assertEqual(loan(30, 20, 750, "F"), "MANUAL REVIEW")


if __name__ == "__main__":
    unittest.main()