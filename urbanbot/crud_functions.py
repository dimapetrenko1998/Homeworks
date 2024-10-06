import sqlite3


def initiate_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        image_url TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


def populate_products():
    products = [
        ("Продукт 1", "Описание продукта 1", 100, "https://thumbs.dreamstime.com/z"
                                                  "/стек-янный-опарник-с-пи-ю-ьками-59031764.jpg"),
        ("Продукт 2", "Описание продукта 2", 200, "https://masterpiecer-images.s3.yandex.net"
                                                  "/188799728db211ee9566d20dae950626:upscaled"),
        ("Продукт 3", "Описание продукта 3", 300, "https://scx2.b-cdn.net/gfx/news/hires/2022/vitamin-pills.jpg"),
        ("Продукт 4", "Описание продукта 4", 400, "https://i.pinimg.com/736x/a9/5c/07"
                                                  "/a95c07941a4f60147ffdd86c8b73ac28.jpg"),
    ]

    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()


def drop_products_table():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Products')
    conn.commit()
    conn.close()


def check_table_structure():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(Products);")
    columns = cursor.fetchall()
    conn.close()
    return columns
