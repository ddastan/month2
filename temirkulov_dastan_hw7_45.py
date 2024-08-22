import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')
conn.commit()

def add_products():
    products = [
        ("Мыло детское", 50.0, 10),
        ("Жидкое мыло с запахом ванили", 75.5, 5),
        ("Шампунь для волос", 120.0, 7),
        ("Зубная паста", 90.0, 15),
        ("Гель для душа", 85.0, 12),
        ("Туалетная бумага", 25.0, 50),
        ("Мочалка для тела", 30.0, 20),
        ("Крем для рук", 110.0, 8),
        ("Лосьон для тела", 130.0, 5),
        ("Пена для ванны", 95.0, 6),
        ("Зубная щетка", 45.0, 25),
        ("Салфетки бумажные", 35.0, 40),
        ("Дезодорант", 150.0, 10),
        ("Крем для лица", 200.0, 3),
        ("Ватные диски", 20.0, 60)
    ]
    cursor.executemany('''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    ''', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('''
    UPDATE products
    SET quantity = ?
    WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('''
    UPDATE products
    SET price = ?
    WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('''
    DELETE FROM products
    WHERE id = ?
    ''', (product_id,))
    conn.commit()

def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def select_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('''
    SELECT * FROM products
    WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)


def search_products_by_title(search_term):
    search_term = f'%{search_term}%'
    cursor.execute('''
    SELECT * FROM products
    WHERE product_title LIKE ?
    ''', (search_term,))
    products = cursor.fetchall()
    for product in products:
        print(product)

add_products()
select_all_products()
update_quantity(1, 20)
update_price(2, 60.0)
delete_product(3)
print("\nТовары после обновлений:")
select_all_products()
print("\nТовары, дешевле 100 сом и количество которых больше 5:")
select_products_by_price_and_quantity(100, 5)
print("\nПоиск товаров по названию 'мыло':")
search_products_by_title('мыло')

conn.close()
