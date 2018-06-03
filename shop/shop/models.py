from datetime import datetime
from pony.orm import Database, Required, Optional, Set, PrimaryKey, sql_debug, show, db_session


#db = Database() # тоже закоментим
# Добавили взамен: 2 строчки
from . import pony

db = pony.db



class Product(db.Entity):
    """Товар"""
    title = Required(str)
    unit = Required(str)
    price = Required(float)
    description = Optional(str)
    category = Required('Category')
    #alt_categories = Set(list('Category'))
    amount = int # количество товара
    history = Set('ProductHistory')
    cartitems = Set('CartItem')
    orderitems = Set('OrderItem')

class ProductHistory(db.Entity):
    """История конкреного товара"""
    product = Required('Product')
    created = Required(datetime, default=datetime.now)
    price = Required(float)


class Category(db.Entity):
    """Категория товара"""
    title = Required(str)
    parent = Optional('Category', reverse='children')
    products = Set('Product')
    children = Set('Category', reverse='parent')


class Customer(db.Entity):
    """Покупатель"""
    email = Required(str, unique=True)
    phone = Optional(str)
    name = Optional(str)
    address = Set('Address')
    cart = Optional('Cart')
    orders = Set('Order')


class Address(db.Entity):
    """Адрес"""
    customers = Set('Customer')
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(str)


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Optional('Customer') or None
    products = Set('CartItem')
    #cart = Set('CartItem')        # ?    #########
    #cartitem = Set('CartItem')     # ?   #######


class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required('Cart')
    product = Required('Product')
    amount = Optional(int, default=1) # 1 единица товара

class Order(db.Entity):
    """Заказ"""
    customer = Required('Customer')
    created = Optional(datetime, default=datetime.now)
    products = Set('OrderItem')  ## ?    ##########
    status = Required('Status')
    cost = Required(float)
    #orderitem = Set('OrderItem')

class Status(db.Entity):
    """Любой статус"""
    name = PrimaryKey(str)
    title = Required(str)
    orders = Set('Order')


class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required('Order')
    product = Required('Product')
    amount = Optional(int, default=1) # 1 единица товара


# sql_debug(True)
#
# db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
# db.generate_mapping(create_tables=True) #, check_tables=True)
#
#
# with db_session:
#     cat_pc = Category(title='ПК')
#     show(cat_pc)
#
#     cat_complect = Category(parent=cat_pc,
#                             title='Комплектующие')
#
# show(cat_complect)