import sqlite3
import os
from sqlite3 import Connection
DB_FILE = os.path.join(os.path.dirname(__file__), 'example.db')
def create_connection(db_file: str) -> Connection:
    conn = sqlite3.connect(db_file)
    return conn
def create_table(conn: Connection) -> None:
    sql = '''CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER
             );'''
    conn.execute(sql)
    conn.commit()
def insert_user(conn: Connection, name: str, age: int) -> int:
    sql = 'INSERT INTO users (name, age) VALUES (?, ?)'
    cur = conn.cursor()
    cur.execute(sql, (name, age))
    conn.commit()
    return cur.lastrowid
def select_all(conn: Connection):
    cur = conn.cursor()
    cur.execute('SELECT id, name, age FROM users')
    return cur.fetchall()
def update_user(conn: Connection, user_id: int, name: str = None, age: int = None) -> int:
    fields = []
    params = []
    if name is not None:
        fields.append('name = ?')
        params.append(name)
    if age is not None:
        fields.append('age = ?')
        params.append(age)
    if not fields:
        return 0
    params.append(user_id)
    sql = 'UPDATE users SET ' + ', '.join(fields) + ' WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    return cur.rowcount
def delete_user(conn: Connection, user_id: int) -> int:
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    return cur.rowcount
def main():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    conn = create_connection(DB_FILE)
    create_table(conn)
    print('Inserting users...')
    Bhuvi_id = insert_user(conn, 'Bhuvi', 21)
    Bhoomi_id = insert_user(conn, 'Bhoomi', 22)
    print('Inserted IDs:', Bhuvi_id, Bhoomi_id)
    print('\nSelecting all users:')
    for row in select_all(conn):
        print(row)
    print('\nUpdating Bhoomi age to 22...')
    update_user(conn, Bhoomi_id, age=22)
    print('After update:')
    for row in select_all(conn):
        print(row)
    print('\nDeleting Bhuvi...')
    delete_user(conn, Bhuvi_id)
    print('After delete:')
    for row in select_all(conn):
        print(row)
    conn.close()
if __name__ == '__main__':
    main()
