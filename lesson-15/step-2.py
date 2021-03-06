# todo: Специальные свойства и методы классов

"""
2.1 Специальные свойства  классов

__name__    - хранит имя класса
__class__   - объект метакласса
__module__  - имя модуля, в котором объявлен данный класс
__bases__   - кортеж базовых классов
__dict__    - словарь атрибутов класса
__doc__     - строка документации
=====================================================

2.2 Специальные свойства и методы объектов

__class__   - класс на основе которого создан объект
__dict__    - словарь свойств объекта (те, которые инициализированы в __init__)
              (если есть __slots__, то не создается словарь)

__dir__()   - метод, хранит список атрибутов класса (используется функцией dir(obj))
__repr__()  - метод, формальное строковое представление объекта (используется функцией repr(obj))
             Должен быть валдным в Python-коде
======================================================

2.3 Явное приведение объекта к определенному типу
Методы:
__bool__    - преобразование в логический тип
__int__     - преобразование в целочисленный тип
__float__   - преобразование в дробный тип с плавающей точкой
__complex__ - преобразование в комплексное число
__str__     - преобразование в строку
__bytes__   - преобразование в байтовую строку (не поддерживается в Python2)
__index__   - преобразование без потерь числового объекта в целочисленный тип
                используется в срезах ([start:end:step])
                => объект используется как индекс (например списка)
                => bin(), oct(), hex()
                => Python2 __oct__, __hex__

"""









