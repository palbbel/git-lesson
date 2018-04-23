# Модули и пакеты

# 1. Импорт модуля целиком

import os.path
import square_shapes


# 2. Чаcтичный импорт

from square_shapes import (calculate_cicle_area, calculate_square_area,
                           calculate_rectangle_area, calculate_triangle_area)
from os import path as Path


# 3. Импорт * (все имена из модуля)
from square_shapes import *

print(square_shapes.calculate_square_area((5)))
print(square_shapes.calculate_rectangle_area(2, 4))

os.path.basename('/home/itmo/1.txt')

print(calculate_rectangle_area(7, 8))


if __name__== '__main__':
    print('Будет работать только если модуль используется как исполняемый (главный)')





