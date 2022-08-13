import unittest
from ben_crist import *
from Calculator import *


class MyTestCase(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(10), 100)
        self.assertAlmostEqual(square(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square('0.1')

        with self.assertRaises(ValueError):
            square(0)
            square(-4)

    def test_circle(self):
        self.assertAlmostEqual(circle(10), 314.15, delta=0.01)
        self.assertAlmostEqual(circle(0.1), 0.0314, delta=0.001)

        with self.assertRaises(TypeError):
            circle('0.1')

        with self.assertRaises(ValueError):
            circle(0)
            circle(-2)

    def test_rectangle(self):
        self.assertEqual(rectangle(10, 9), 90)
        self.assertAlmostEqual(rectangle(10, 0.5), 5, delta=0.01)
        self.assertAlmostEqual(rectangle(1.5, 10), 15, delta=0.01)
        self.assertAlmostEqual(rectangle(3.5, 1.5), 5.25, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle('0.1', 1)
            rectangle('0.1', '1')
            rectangle(0.1, '1')

        with self.assertRaises(ValueError):
            rectangle(1, 0)
            rectangle(0, 1)
            rectangle(0, 0)
            rectangle(-1, 1)
            rectangle(1, -1)
            rectangle(-1, -1)

    def test_triangle(self):
        self.assertEqual(triangle(10, 9), 45)
        self.assertAlmostEqual(triangle(10, 0.8), 4, delta=0.01)
        self.assertAlmostEqual(triangle(1.2, 10), 6, delta=0.01)
        self.assertAlmostEqual(triangle(5.5, 2.5), 6.875, delta=0.0001)

        with self.assertRaises(TypeError):
            triangle('0.1', 1)
            triangle('0.1', '1')
            triangle(0.1, '1')

        with self.assertRaises(ValueError):
            triangle(1, 0)
            triangle(0, 1)
            triangle(0, 0)
            triangle(-1, 1)
            triangle(1, -1)
            triangle(-1, -1)

    def test_trapezoid(self):
        self.assertEqual(trapezoid(4, 5, 6), 27)
        self.assertAlmostEqual(trapezoid(10, 0.8, 5), 27, delta=0.01)
        self.assertAlmostEqual(trapezoid(1.2, 10, 6), 33.6, delta=0.01)
        self.assertAlmostEqual(trapezoid(5.5, 2.5, 7), 28, delta=0.01)
        self.assertAlmostEqual(trapezoid(3.5, 2.9, 3.4), 10.88, delta=0.001)

        with self.assertRaises(TypeError):
            trapezoid('0.1', 1, 1)
            trapezoid('0.1', '1', 1)
            trapezoid(0.1, '1', 1)
            trapezoid(0.1, 1, '1')
            trapezoid(0.1, '1', '1')
            trapezoid('0.1', '1', '1')

        with self.assertRaises(ValueError):
            trapezoid(1, 0, 1)
            trapezoid(0, 1, 1)
            trapezoid(1, 1, 0)
            trapezoid(0, 0, 0)
            trapezoid(-1, 1, 1)
            trapezoid(1, -1, 1)
            trapezoid(1, 1, -1)
            trapezoid(-1, -1, 1)

    def test_ellipse(self):
        self.assertAlmostEqual(ellipse(10, 11), 345.575, delta=0.001)
        self.assertAlmostEqual(ellipse(0.5, 11), 17.27, delta=0.01)
        self.assertAlmostEqual(ellipse(10, 0.8), 25.13, delta=0.01)
        self.assertAlmostEqual(ellipse(5.5, 6.7), 115.767, delta=0.001)

        with self.assertRaises(TypeError):
            ellipse('0.1', 1)
            ellipse(0.1, '1')
            ellipse('0.1', '1')

        with self.assertRaises(ValueError):
            ellipse(0, 1)
            ellipse(1, 0)
            ellipse(0, 0)
            ellipse(-1, 1)
            ellipse(1, -1)
            ellipse(-1, -1)

    def test_power(self):
        self.assertEqual(power(8, 2), 64)
        self.assertAlmostEqual(power(1.5, 3), 3.375, delta=0.01)

        with self.assertRaises(TypeError):
            power('0.1', 1)
            power(0.1, '1')
            power('0.1', '1')
            power(1, 0.1)
            power(0.1, 0.1)

        with self.assertRaises(ValueError):
            power(0, 1)
            power(1, 0)
            power(0, 0)
            power(1, -1)
            power(-1, -1)

    def test_factorial(self):
        self.assertEqual(factorial(3), 6)

        with self.assertRaises(TypeError):
            factorial('0.1')
            factorial(0.1)

        with self.assertRaises(ValueError):
            factorial(0)
            factorial(-2)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(0.5), 0.707, delta=0.001)

        with self.assertRaises(TypeError):
            square_root('0.1')

        with self.assertRaises(ValueError):
            square_root(0)
            square_root(-2)


if __name__ == '__main__':
    unittest.main()
