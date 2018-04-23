from math import pi as PI

# что будет импортировано если в другом месте использовали import *
__all__ = ['calculate_square_area', # что будет импортировано если в другом месте использовали import *
           'calculate_rectangle_area',
           'calculate_triangle_area',
           'calculate_cicle_area'] # что будет импортировано если в другом месте использовали import *


def calculate_square_area(a):
    """ Возвращает площадь квадрата."""
    return a ** 2


def calculate_rectangle_area(a, b):
    """ Площадь прямоугольника"""
    return a * b


def calculate_triangle_area(a, b, c):
    """ Формула Герона"""
    p = (a + b + c)/2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculate_cicle_area(r):
    return 3.14 * r ** 2
    return PI * r ** 2


