import math


def power(num, pow) -> int:
    """
    Method to calculate the power of a number
    :param num: The number being raised to a certain power
    :param pow: The power that the number will be raised to
    :return: The value of the number to the given power
    """
    if type(num) != int and type(pow) != int:
        raise TypeError('Not a whole number')
    if pow <= 0 and num == 0:
        raise ValueError('Not positive exponent')
    if pow == 1:
        return num
    else:
        return num * power(num, pow - 1)


def factorial(num) -> int:
    """
    Method to calculate the factorial of a given number
    :param num: The number that the factorial will be found for
    :return: The factorial of the number
    """
    if type(num) != int:
        raise TypeError('Not a whole number')
    if num <= 0:
        raise ValueError('Not positive')
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


def square_root(num) -> float:
    """
    A method to find the square root of a number
    :param num: The number that the square root will be found for
    :return: The square root of the number
    """
    if type(num) != int and type(num) != float:
        raise TypeError('Not a numeric input')
    if num <= 0:
        raise ValueError('Not positive')
    return math.sqrt(num)


