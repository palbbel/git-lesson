class BaseConfig(object):
    SECRET_KEY = 'Random string'
    WTF_CSRF_SECRET_KEY = 'Random string'


class DevConfig(BaseConfig):
    PONY = {
        'provider': 'sqlite',
        'dbname': 'database.sqlite'
    }


class ProdConfig(BaseConfig):
    PONY = {
        'provider': 'mysql',
        'user': 'root',
        'pass': 'toor',
        'dbname': 'database.sqlite'
    }
