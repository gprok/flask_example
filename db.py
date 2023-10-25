import sqlite3
import os
from models import Product

def get_connection():
    con = sqlite3.connect('products.db')
    return con

def create_db():
    if not os.path.isfile('products.db'):
        con = get_connection()
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 price NUMERIC)
            """)
        con.commit()
        con.close()


def get_all_products():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    products = []
    for p in result:
        product = Product(p[0], p[1], p[2])
        products.append(product)
    return products


def get_product(pid):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (pid,))
    result = cursor.fetchone()
    print(result) 
    product = Product(result[0], result[1], result[2])
    return product


def add_new_product(name, price):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    con.commit()
    con.close()