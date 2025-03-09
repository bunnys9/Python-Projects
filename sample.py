import sqlite3 as sql
from contextlib import contextmanager
import logging

logging.basicConfig(level=logging.INFO)

@contextmanager
def connection():
    with sql.connect("launch.db") as conn:
        yield conn

def create_table():
    try:
        with connection() as conn:
            table_query = 'create table if not exists launchpad(name varchar(20) not null, empid integer primary key not null, salary integer not null)'
            cur = conn.cursor()
            cur.execute(table_query)
            logging.info("Successfully Created Table: Launchpad")

    except Exception as e:
        logging.error(str(e))

def insert_data():
    try:
        with connection() as conn:
            name = input("Enter your Name : ")
            empid = int(input("Enter your Employee ID : "))
            salary = int(input("Enter your Salary : "))
            data_query = 'insert into launchpad values(?,?,?)'
            cur = conn.cursor()
            cur.execute(data_query,(name, empid, salary))
            conn.commit()
            logging.info("Successfully Inserted date into Table: Launchpad")

    except Exception as e:
        logging.error(e)

def read_data():
    try:
        with connection() as conn:
            select_data = 'select * from launchpad'
            cur = conn.cursor()
            result = cur.execute(select_data)
            for item in result:
                for details in item:
                    print(details,end="\t")
                print()
    except Exception as e:
        logging.error(e)

def update_data():
    try:
        with connection() as conn:
            empid = int(input("Enter whose details want to update : "))
            name= input("Enter your name : ")
            update_query = 'update launchpad set name = ? where empid =?'
            cur = conn.cursor()
            cur.execute(update_query, (name, empid))
            conn.commit()
            logging.info("Updated details Successfully")

    except Exception as e:
        logging.error(str(e))

def delete_data():
    try:
        with connection() as conn:
            empid = int(input("Enter your Emp ID : "))
            delete_query = 'delete from launchpad where empid =?'
            cur = conn.cursor()
            cur.execute(delete_query, (empid,))
            conn.commit()
            logging.info("Deleted details Successfully")

    except Exception as e:
        logging.error(str(e))


choice = 'yes'
menu = """
1.  Insert Data
2.  Read All Data
3.  Update Data
4.  Delete Data
"""

while (choice=='yes'):
    print(menu)
    print()
    try:
        ch = int(input("Enter your Choice : "))
        try:      
            if ch==1:
                insert_data()
            elif ch==2:
                read_data()
            elif ch==3:
                update_data()
            elif ch==4:
                delete_data()
            else:
                print("Invalid Input")
                
            choice =input("Do you want to continue  [yes/no] : ")
            
        except:
            print("invali input, Kindly try again")
        
    except Exception as e:
        logging.error("Invalid Choice, Kindly Try again")
        break
#create_table()
#   
#update_data()
#read_data()
#delete_data()
#read_data()
