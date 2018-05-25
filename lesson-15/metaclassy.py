# Метаклассы

def person_init(self, firsname, lastname):
    self.firsname = firsname
    self.lastname = lastname


"""
type принимает три аргумента:
- имя нового типа
- кортеж базовых типов
- словарь атрибутов

"""

Person = type('Person', (object,), {
    '__init__': person_init,
    '__str__': lambda self: '{} {}'.format(self.firsname, self.lastname)
})

print(type(Person), Person)



def car_init(self, vendor, driver):
    self.vendor = vendor
    self.driver = driver


Car = type('Car', (object,), {   # наследуем от object
    'COLOR_RED': 1,
    '__init__': car_init,
    'get_vendor': lambda self: self.vendor,
    'get_driver': lambda self: self.driver
})

print(type(Car), Car)


driver = Person('Михаэль', 'Шумахер')
ferrari = Car('Ferrari', driver)


print('Автомобиль "{}", водитель "{}"'.format(ferrari.get_vendor(), ferrari.get_driver()))



# todo: Demo метакласс

class DemoMeta(type):  # наследуем от type (создаем метакласс)
    def __new__(mcs, name, bases, d):    # всегда статический метод  (теже три аргумента)
        print('Выделение памяти под класс:\n', name, bases, d)
        return super().__new__(mcs, name, bases, d)

    def __init__(cls, name, bases, d):
        print('Инициализация класса:\n', name, bases, d)
        super().__init__(name, bases, d)

    def __call__(cls, *args, **kwargs):
        print('Создание экземпляра (объекта):\n', args, kwargs)
        return super().__call__(*args, **kwargs)


class Demo(metaclass=DemoMeta):
    # Переопределим все (это не рекомендуется делать)
    def __new__(cls, *args, **kwargs):
        print('Выделение памяти под экземпляр (объект):\n', args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Инициализация экземпляра (объекта):\n', args, kwargs)

    # def __call__(self, *args, **kwargs):
    #     print('Инициализация экземпляра (объекта):\n', args, kwargs)
    #     return super().__call__(self)

demo = Demo(1, True, msg='Ok')

demo = Demo(444, False, msg='Not Ok')

demo = Demo.__call__(44411, False, 'fdgdfg', msg='Not Ok111')




# todo: Пример № 2
from abc import ABCMeta, abstractclassmethod

# добавляем метакласс, смотри причину ниже, чтобы выдавал ошибку при неправильном создании класса
class MathFunctionMeta(ABCMeta):
    def __init__(cls, name, bases, d):
        super().__init__(name, bases, d)

        if bases: # если есть, то пытаемся создать дочерний класс и тогда проверяем свойство (можем проверять много свойств)
            cls.check_property('func_name')


    def check_property(cls, prop):
        if getattr(cls, prop, None) is None:       # новый метод (при свойстве или его название (атрибуте или его название) в переменной)
            raise RuntimeError('You need to setthe "{}" property'.format(prop))

#=====================

class MathFunction(metaclass=MathFunctionMeta): # после добавления того что выше добавляем metaclass=MathFunctionMeta
    #func_name = None # так как возникла ошибка после добавления метакласса, сюда вписываем значение
    func_name = 'round'

    def get_func_name(self):
        return self.func_name

    @abstractclassmethod
    def execute(self):
        pass


class RoundFunction(MathFunction):


    def __init__(self, number, ndigits=None):
        self.number = number
        self.ndigits = ndigits

    def execute(self):
        return  round(self.number, self.ndigits)


print(RoundFunction(50).get_func_name())    # что то забыли вернуло None, чтобы исправить нужен макласс,
                                            #  его и сделаем (придется сделать из двухметаклассов) или унаследуем
                                            # будем наследовать, будем вклиниваться до создания класса

                                            # после добавления метакласса возникла ошибка по raise
                                            # затем меняем func_name = None на func_name = 'round'
                                            # вернуло "round"

