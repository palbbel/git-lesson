import os
from abc import *


class ParamHandler(metaclass=ABCMeta):

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            pass  #raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            pass  #raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass) )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            pass #raise ParamHandlerException('Type "{}" not found!'.format(ext)            )
        return klass(source, *args, **kwargs)


class TextParamHandler(ParamHandler):
    def read(self):
        """
        Чтение из текстового файла и присвоение значений в self.params
        """
    def write(self):
        """
        Запись в текстовый файл параметров self.params
        """
class XmlParamHandler(ParamHandler):

    def read(self):
        """
        Чтение в формате XML и присвоение значений в self.params
         """

    def write(self):
        """
        Запись
        """

if __name__ == '__main__':
    # config = ParamHandler.get_instance('./params.xml')
    # config.add_param('key1', 'val1')
    # config.add_param('key2', 'val2')
    # config.add_param('key3', 'val3')
    #config.write()  # запись файла в XML формате
    #config = ParamHandler.get_instance('./params.txt')
    #config.read()

    ParamHandler.add_type('json', 'json')