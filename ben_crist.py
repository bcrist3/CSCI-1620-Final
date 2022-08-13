import math


def circle(radius) -> float:
    """
    A method to calculate the area of a circle
    :param radius: The radius for the circle
    :return: The area of the circle
    """
    if type(radius) != int and type(radius) != float:
        raise TypeError('Not numeric input')
    if radius <= 0:
        raise ValueError('Not positive')
    return math.pi * (radius * radius)


def rectangle(length, width) -> float:
    """
    Method to calculate the area of a rectangle
    :param length: The length of the rectangle
    :param width: The width of the rectangle
    :return: The area of the rectangle
    """
    if type(length) != int and type(length) != float and type(width) != int and type(width) != float:
        raise TypeError('Not numeric input')
    if length <= 0 and width <= 0:
        raise ValueError('Not positive')
    return length * width


def square(length) -> float:
    """
    Method to calculate the area of a square
    :param length: The side length of the square
    :return: The area of the square
    """
    if type(length) != int and type(length) != float:
        raise TypeError('Not numeric input')
    if length <= 0:
        raise ValueError('Not positive')
    return length * length


def triangle(base, height) -> float:
    """
    Method to calculate the area of a triangle
    :param base: The base of the triangle
    :param height: The height of the triangle
    :return: The area of the triangle
    """
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError('Not numeric input')
    if base <= 0 and height <= 0:
        raise ValueError('Not positive')
    return (1 / 2) * base * height


def trapezoid(base1, base2, height) -> float:
    """
    Method to calculate the area of a trapezoid
    :param base1: The first base of the trapezoid
    :param base2: The second base of the trapezoid
    :param height: THe height of the trapezoid
    :return: The area of the trapezoid
    """
    if type(base1) != int and type(base1) != float and type(height) != int and type(height) != float and type(base2) \
            != int and type(base2) != float:
        raise TypeError('Not numeric input')
    if base1 <= 0 and base2 <= 0 and height <= 0:
        raise ValueError('Not positive')
    return ((base1 + base2) / 2) * height


def ellipse(radius1, radius2) -> float:
    """
    Method to calculate the area of an ellipse
    :param radius1: The horizontal radius of the ellipse
    :param radius2: The vertical radius of the ellipse
    :return: The area of the ellipse
    """
    if type(radius1) != int and type(radius1) != float and type(radius2) != int and type(radius2) != float:
        raise TypeError('Not numeric input')
    if radius1 <= 0 and radius2 <= 0:
        raise ValueError('Not positive')
    return math.pi * radius1 * radius2

