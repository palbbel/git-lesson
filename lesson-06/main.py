# Базы данных

import sqlite3

# 1. Подключение к БД
conn = sqlite3.connect('db.sqlite')

# 2. Создание объекта курсора
cursor = conn.cursor()

# 3. Запрос к БД
sql = '''
    CREATE TABLE IF NOT EXISTS shortener (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      original_url TEXT NOT NULL,
      short_url TEXT NOT NULL DEFAULT '',
      created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
'''
cursor.execute(sql)
conn.commit()

sql = '''
    INSERT INTO shortener (original_url) VALUES (?)
'''

cursor.execute(sql, ('http://profi.itmo.ru',))  # если одно значение вставлям (вместо ?), то запятая
                                                # обязательна
conn.commit()
# DMl - select, insert, update, delete и другие



sql = '''
    SELECT id, original_url, short_url, created FROM shortener
'''

# выборка данных
cursor.execute(sql)
resault = cursor.fetchall()
print(resault)

# 4. Закрываем соединение
conn.close()




# Контекстный менеджер (комитеть не надо, закрывать не надо) при работе с ресурсами
'''
try:
    ...
finally:
    ...
'''
with sqlite3.connect('db.sqlite') as conn:
    sql = 'SELECT * from shortener'
    cursor = conn.execute()  # Курсор создавать специально не обязательно
    print(cursor.fetchall())