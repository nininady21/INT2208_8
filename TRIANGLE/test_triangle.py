import unittest
from triangle import classifyTriangle

class TestTriangle(unittest.TestCase):

    def test_invalid_negative(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), "Invalid input")

    def test_invalid_over_100(self):
        self.assertEqual(classifyTriangle(100, 101, 200), "Invalid input")

    def test_invalid_not_integer(self):
        self.assertEqual(classifyTriangle(-1.1, 1.3, 1), "Invalid input")

    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 1), "Not a triangle")

    def test_Equilateral_triangle(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral triangle")
    
    def test_Isosceles_triangle(self):
        self.assertEqual(classifyTriangle(3, 3, 4), "Isosceles triangle")
    
    def test_Scalene_triangle(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Scalene triangle")
    
if __name__ == "__main__":
    unittest.main()