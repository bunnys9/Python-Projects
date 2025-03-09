import sqlite3 as sql
from contextlib import contextmanager

@contextmanager
def connection():
    conn = sql.connect("sqlite.db")
    yield conn

def table():
    with connection() as conn:
        cur = conn.cursor()
        create_table = 'create table if not exists employee(empid integer primary key autoincrement, name varchar(20))'
        cur.execute(create_table)

def data():
    with connection() as conn:
        cur= conn.cursor()
        insert_data = 'insert into employee(name) values("deepika")'
        cur.execute(insert_data)
        conn.commit()


def read():
    with connection() as conn:
        cur = conn.cursor()
        retrieve_data = 'select * from employee'
        res = cur.execute(retrieve_data)

        for i in res:
            print(i)

#table()
#data()
read()