# для распространения и установки (оба файла main не должено быть)
from setuptools import setup
"""
name        - название пакета
version     - версия пакета (0.0.0)
description - описание пакета
url         - URL-адрес сайта
license     - Лицензия
author      - Имя автора
author_email- E-mail автора

packages    - пакеты, которые надо скопировать при установке (без рекурсии копирование, необходимо указать
        вложенные пакеты)

py_modules  - модули, которые надо скопировать при установке

scripts     - запускаемые из командной строки скрипты

install_requires - список зависимостей (появился в setuptools, в distutils не было) для пакетного
                    менеджера, чтобы установить все зависимости из pypi.org


Утилита
Пакетный менеджер - pip

"""

setup(
    name='mega-math',  # дефис более нагляден
    version='0.0.1',
    description='Information',
    url='https://github.com/user/mega-math',
    license='Apache-2.0',
    author='Pavel Belyakov',
    author_email='palb@yandex.ru',
    packages=[
        'mega_math',   # тут точное название
    ]




)