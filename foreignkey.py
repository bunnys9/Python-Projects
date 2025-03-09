import sqlite3 as sql
import logging

logging.basicConfig(level=logging.INFO)
conn = sql.connect("infy.db")
if conn:
    logging.info("Connected to DB Successfully")
else:
    logging.error("Not connected to Database, please try again")

cur = conn.cursor()
cur.execute("PRAGMA foreign_keys=ON")


table1 = 'create table if not exists users(name varchar(10) not null, order_id int primary key not null)'
cur.execute(table1)

table2 = 'create table if not exists orders(order_id int primary key not null, price int not null, foreign key (order_id) references users(order_id) on delete cascade)'

cur.execute(table2)

data = 'insert into orders(order_id, price) values(?, ?)'
cur.execute(data,(4567, 900))

read = 'select users.name, users.order_id, orders.price from users inner join orders on users.order_id=orders.order_id'
res = cur.execute(read)

for i in res:
    print(i)



conn.commit()


cur.close()
conn.close()

