# Пакеты
import mega_math.square_shapes
mega_math.square_shapes.calculate_square_area(2)

from mega_math import square_shapes
square_shapes.calculate_cicle_area(10)

from mega_math.square_shapes import calculate_triangle_area
calculate_triangle_area(1, 2, 3)


# Относительный импорт (только в модуле, не ав исполняемом файле)
# from . import module_name
# from .module_name import class_name
# from ..parent_module import class_name


from mega_math import calculate_cicle_area
print(calculate_cicle_area(10))