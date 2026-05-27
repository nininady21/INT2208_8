import unittest
from loan import loan


class TestLoan(unittest.TestCase):

    def test_TC1(self):
        self.assertEqual(
            loan(17, 20, 700, "C"),
            "Invalid Input"
        )

    def test_TC2(self):
        self.assertEqual(
            loan(66, 20, 700, "C"),
            "Invalid Input"
        )

    def test_TC3(self):
        self.assertEqual(
            loan(30, 4.9, 700, "C"),
            "Invalid Input"
        )

    def test_TC4(self):
        self.assertEqual(
            loan(30, 500.1, 700, "C"),
            "Invalid Input"
        )

    def test_TC5(self):
        self.assertEqual(
            loan(30, 20, 299, "C"),
            "Invalid Input"
        )

    def test_TC6(self):
        self.assertEqual(
            loan(30, 20, 851, "C"),
            "Invalid Input"
        )

    def test_TC7(self):
        self.assertEqual(
            loan(30, 20, 700, "X"),
            "Invalid Input"
        )

    def test_TC8(self):
        self.assertEqual(
            loan("30", 20, 700, "C"),
            "Invalid Input"
        )

    def test_TC9(self):
        self.assertEqual(
            loan(30, 20, 400, "C"),
            "REJECT"
        )

    def test_TC10(self):
        self.assertEqual(
            loan(30, 10, 600, "C"),
            "REJECT"
        )

    def test_TC11(self):
        self.assertEqual(
            loan(30, 10, 750, "F"),
            "REJECT"
        )

    def test_TC12(self):
        self.assertEqual(
            loan(30, 10, 750, "C"),
            "MANUAL REVIEW"
        )

    def test_TC13(self):
        self.assertEqual(
            loan(30, 20, 600, "C"),
            "APPROVE"
        )

    def test_TC14(self):
        self.assertEqual(
            loan(30, 20, 600, "F"),
            "MANUAL REVIEW"
        )

    def test_TC15(self):
        self.assertEqual(
            loan(30, 20, 750, "C"),
            "APPROVE"
        )

    def test_TC16(self):
        self.assertEqual(
            loan(30, 20, 750, "F"),
            "MANUAL REVIEW"
        )


if __name__ == "__main__":
    unittest.main()