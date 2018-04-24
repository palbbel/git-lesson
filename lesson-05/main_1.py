# Модули и пакеты

# 1. Импорт модуля целиком

import os.path

from mega_math import square_shapes
from mega_math.square_shapes import *

print(square_shapes.calculate_square_area((5)))
print(square_shapes.calculate_rectangle_area(2, 4))

os.path.basename('/home/itmo/1.txt')

print(calculate_rectangle_area(7, 8))

###### nuitka


if __name__== '__main__':
    print('Будет работать только если модуль используется как исполняемый (главный)')





