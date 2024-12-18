import sqlite3

connection = sqlite3.connect('bot_telegram.db')
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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL
    balance INTEGER NOT NULL
    );
    ''')

    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

    connection.commit()


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.commit()
    return products


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))
    connection.commit()


def is_included(username):
    cursor.execute(f'SELECT username FROM Users')
    users = cursor.fetchall()
    connection.commit()
    incl = False
    for i in users:
        if i[0] == username:
            incl = True
    return incl