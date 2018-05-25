#! /usr/bin/env python
# -*- coding: utf-8 -*-




# todo: Классы и объекты

# Как объявить.создать класс
# Свойства/атрибуты/данные
# В свойствах хранятся данные объекта

# todo: Зачем нужен коструктор?
# Для инициализации объекта
#метод - поведения объекта
firstname = None
lastname = None
class Person(object):

    __slots__ = ('__firstname', '__lastname') # определяет свойства и нельзя менять на лету
                                              # и нельзя добавлять свойства на лету
                                              # не создает dict

    def  __init__(self, firstname, lastname):  # метод
        # self - ссылка на текущий объект
        self.__firstname = firstname # __ вроде как нельзя изментть, псевдозащита от изменения
        self.__lastname = lastname


    def get_full_name(self):
        return '{} {}'.format(self.get_firstname, self.get_firstname)

    def get_firstname(self):
        # Метод получатель - getter
        return self.__firstname

    #def set_firstname(self, firstname):
    #    # Ьуещв установщик - setter
    #    self.firstname = firstname


    def get_lastname(self):
        # Ьуещв получатель - getter
        return self.__lastname


# Как создать объект/экземпляр

linus = Person('Linus', 'Torvalds')
#linus.firstname = 'Linus'
#linus.lastname = 'Torvalds'
print(linus.get_firstname, linus.get_firstname) # Чтение свойств

#print(Person, linus)
#print(type(Person), type(linus))

stallman = Person('Richard', 'Stallman')
print(stallman.get_firstname, stallman.get_firstname)
#=============================================
print(linus.get_full_name())
print(stallman.get_full_name())
#print(linus.__dict__)   ### {'_Person__lastname': 'Torvalds', '_Person__firstname': 'Linus'}


# todo: Что такое наследование


class Developer(Person): # от какого класса наследуем
    """
    Person - родительский класс или базовый
    Developer - дочерний класс
    """
    # при наследовании слоты теряются поэтому дописываем
    __slots__ = ('__skills',) # учитываются и из родительского вроде

    def __init__(self, firstname, lastname, skills):
        super().__init__(firstname, lastname) # переопределили родительский конструктор Person (3 Python)
        #super(Developer, self).__init__(firstname, lastname)  # для второго Python
        self.__skills = skills #or [] # по умолчанию


    def  add_skills(self, skill):
        if skill not in self.get_skills():
            self.get_skills().append(skill)

    def get_skills(self):
        return self.__skills

    def remove_skill(self, skill):
        if skill in self.get_skills():
            self.get_skills().remove(skill)




dev_2 = Developer('Developer', '2', ['Brainfuck'])
print(dev_2.get_skills())
#print(dev_2.get_firstname())
print(dev_2.get_full_name())
print(dev_2.get_skills())

# todo: Статические свойства и методы
# Свойства и методы класс

class Singleton(object):
    __instance = None # статическое свойство  - общее для всех экземпляров
                       # если меняется меняется для всех

    def __init__(self):
        self.__params = {}


    @classmethod  # статический метод
    def get_instance(cls):  # cls выходит само
        if cls.__instance is None:
            cls.__instance = cls() # вызываем конструктор данного класс, создаем экземпляр
        return cls.__instance      # или возвращаем уже созданный


    def add_param(self, key, value):
        self.__params[key] = value

    def get_param(self,key):
        return self.__params.get(key)

    def remove_param(self, key):
        if key in self.__params:
            self.get_param().remove(key)

Singleton.get_instance()  # объект не создавали


# Экземпляр всегда один  (поэтому и называтся одиночка)
config = Singleton.get_instance()
config.add_param('db_host', 'localhost')
config.add_param('db_port', 1234)

config_2 = Singleton.get_instance()
print(config_2.get_param('db_host'))
print(config_2.get_param('db_port'))

print(config_2 is config)



