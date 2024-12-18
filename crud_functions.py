import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    );
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_title ON PRODUCTS (title)')
    connection.commit()


def get_all_products():
    initiate_db()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products
