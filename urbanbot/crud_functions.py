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
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
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


def check_tables():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Существующие таблицы:", tables)
    conn.close()


def add_user(username, email, age):
    try:
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Users (username, email, age) VALUES (?, ?, ?)
        ''', (username, email, age))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Пользователь с email {email} уже существует.")
    finally:
        conn.close()


def is_included(username):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user is not None


def user_exists(email):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Users WHERE email = ?', (email,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists
