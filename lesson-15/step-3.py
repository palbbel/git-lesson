# 2.4 Перегрузка операторов

class Vector(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)


    def __add__(self, other):  # перегружает оператор сложения, новую реализацию дает
        """перегрузка оператора +"""
        assert isinstance(other, Vector)  # надо проверить other это вектор или нет
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # перегружает оператор вычитания, новую реализацию дает
        """перегрузка оператора - """
        assert isinstance(other, self.__class__)  # надо проверить other это вектор или нет
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # перегружает оператор уьножения, новую реализацию дает
        """перегрузка оператора * """
        assert isinstance(other, self.__class__)  # надо проверить other это вектор или нет
        return Vector(self.x * other.x, self.y * other.y)

    def __gt__(self, other):  # перегружает оператор сравнения, новую реализацию дает ОПЕРАТОР БОЛЬШЕ (левый больще правого)
        """перегрузка оператора > """
        assert isinstance(other, self.__class__)  # надо проверить other это вектор или нет
        return self.lenght > other.lenght

    def __eq__(self, other):  # перегружает оператор сравнения, новую реализацию дает ОПЕРАТОР БОЛЬШЕ (левый больще правого)
        """перегрузка оператора == """
        assert isinstance(other, self.__class__)  # надо проверить other это вектор или нет
        return self.lenght == other.lenght

    def __ge__(self, other):  # перегружает оператор сравнения, новую реализацию дает ОПЕРАТОР БОЛЬШЕ (левый больще правого)
        """перегрузка оператора >= """
        assert isinstance(other, self.__class__)  # надо проверить other это вектор или нет
        return self.lenght >= other.lenght

    @property  # превращает метод в свойство
    def lenght(self):
        return (self.x **2 + self.y ** 2) ** 0.5



v1 = Vector(-3, 4)
print(v1)

v2 = Vector(-3, 6)

v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2
print('Сумма векторов: ', v3)
print('Разность векторов: ', v4)
print('Произведение: ', v5)


#v1+1
