import unittest
from triangle import classifyTriangle

class TestTriangle(unittest.TestCase):

    # TC01
    def test_TC01(self):
        self.assertEqual(classifyTriangle(0, 5, 5), "Invalid input")

    # TC02
    def test_TC02(self):
        self.assertEqual(classifyTriangle(1, 5, 5), "Isosceles triangle")

    # TC03
    def test_TC03(self):
        self.assertEqual(classifyTriangle(101, 5, 5), "Invalid input")

    # TC04
    def test_TC04(self):
        self.assertEqual(classifyTriangle(100, 100, 100), "Equilateral triangle")

    # TC05
    def test_TC05(self):
        self.assertEqual(classifyTriangle(-1, 5, 5), "Invalid input")

    # TC06
    def test_TC06(self):
        self.assertEqual(classifyTriangle(5.5, 5, 5), "Invalid input")

    # TC07
    def test_TC07(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "Not a triangle")

    # TC08
    def test_TC08(self):
        self.assertEqual(classifyTriangle(2, 2, 5), "Not a triangle")

    # TC09
    def test_TC09(self):
        self.assertEqual(classifyTriangle(10, 1, 1), "Not a triangle")

    # TC10
    def test_TC10(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral triangle")

    # TC11
    def test_TC11(self):
        self.assertEqual(classifyTriangle(100, 100, 100), "Equilateral triangle")

    # TC12
    def test_TC12(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "Not a triangle")

    # TC13
    def test_TC13(self):
        self.assertEqual(classifyTriangle(5, 5, 3), "Isosceles triangle")

    # TC14
    def test_TC14(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Scalene triangle")


if __name__ == "__main__":
    unittest.main()