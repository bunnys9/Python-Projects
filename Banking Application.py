print()
print("-----------------------------")
print("    Welcome to Bunny Bank")
print("-----------------------------")


a = """
     1.  Create Account
     2.  Update KYC
     3.  Deposit
     4.  Withdraw
     5.  Check Balance
     6.  Account Details
     7.  Delete Account"""


b = """

Enter your Choice number to update the KYC:

1.  Name
2.  Date of Birth
3.  Phone Number
4.  Address"""
cust_list=[]
def custnum():
     import random
     acc_num = list(map(int,range(1000,1100,5)))
     
     cust = random.choice(acc_num)
     #cust_list.append(cust)
     acc_num.remove(cust)
     #print(cust_list)
     return cust

def dis(num):
     
     details = 'select * from customers where cust_acc = ?'
     
     cur.execute(details,(num,))
     
     res = cur.fetchall()
     print()
     print()
     print("Account Number : ", res[0][0])
     print("Name           : ", res[0][1])
     print("Date of Birth  : ", res[0][2])
     print("Phone Number   : ", res[0][3])
     print("Address        : ", res[0][4])
     print(f"Balance        :  Rs.{res[0][5]}/-")
import sqlite3 as sql

conn = sql.connect("Bank_Bunny.db")
table = 'create table if not exists customers(cust_acc int primary key, name text, dob date, ph int(10), address text, bal int)'
cur   = conn.cursor()
cur.execute(table)

def create():
     x = custnum()
     
     bal = 0
     details = 'insert into customers values(?, ?, ?, ?, ?, ?)'
     name    = input("Enter your Name         : ")
     dob     = input("Enter your DOB          : ")
     ph      = input("Enter your Phone Number : ")
     address = input("Enter your Address      : ")

     print("Your Account Number     : ", x)
     cur.execute(details,(x, name,dob,ph,address,bal))
     conn.commit()

def display():
     num = int(input("\nEnter your account number : "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
               dis(num)

     except:
          print("\nInvalid Account Number, Kindly Try Again")


def modify():
     num = int(input("\nEnter your account number : "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()

          
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
          
               
               dis(num)
               
               print(b)
               print()
               ch = int(input("Enter your Option : "))
               if ch==1:
                    name = input("Enter Updated Name : ").capitalize()

                    details = 'update customers set name = ? where cust_acc = ?'

                    

                    cur.execute(details,(name,num))
                    conn.commit()

                    print("\nBelow are the Updated Details of Account Number : ",num)
                    dis(num)

               elif ch==2:
                    dob = input("Enter Updated DOB : ")

                    details = 'update customers set dob = ? where cust_acc = ?'

                    

                    cur.execute(details,(dob,num))
                    conn.commit()

                    print("\nBelow are the Updated Details of Account Number : ",num)
                    dis(num)

               elif ch==3:
                    ph = int(input("Enter Updated Phone Number : "))

                    details = 'update customers set ph = ? where cust_acc = ?'

                    

                    cur.execute(details,(ph,num))
                    conn.commit()

                    print("\nBelow are the Updated Details of Account Number : ",num)
                    dis(num)

               elif ch==4:
                    address = input("Enter Updated Address : ").capitalize()

                    details = 'update customers set address = ? where cust_acc = ?'

                    

                    cur.execute(details,(address,num))
                    conn.commit()

                    print("\nBelow are the Updated Details of Account Number : ",num)
                    dis(num)
               else:
                    print("\nInvalid Input, Try Again")
     except:
          print("\nInvalid Account Number, Kindly Try Again")

def deposit():
     num = int(input("\nEnter your account number : "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()

          
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
          
               
               amount = int(input("How much do you want to deposit : "))
               
               details = 'update customers set bal = bal+? where cust_acc = ?'

               cur.execute(details,(amount,num))
               conn.commit()
               
               print("\nBelow are the Updated Details of Account Number : ",num)
               dis(num)
     except:
          print("\nInvalid Account Number, Kindly Try Again")


def withdraw():
     num = int(input("\nEnter your account number : "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()

          
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
          

               amount = int(input("How much do you want to Withdraw : "))

               details = 'select * from customers where cust_acc = ?'

               cur.execute(details,(num,))

               res = cur.fetchall()
          

               if res[0][5]>=amount:
               
                    detail = 'update customers set bal = bal-? where cust_acc = ?'

                    cur.execute(detail,(amount,num))
                    conn.commit()
                    
                    print("\nBelow are the Updated Details of Account Number : ",num)
                    dis(num)
                    
               elif res[0][5] < amount:
                    print("Insufficient Funds")
     except:
          print("\nInvalid Account Number, Kindly Try Again")

def check():
     num = int(input("\nEnter your account number : "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()
          
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
          
               
               details = 'select bal from customers where cust_acc = ?'

               bal = cur.execute(details,(num,))
               res = cur.fetchall()

               print(f"\nBalance : Rs.{res[0][0]}/-")

               conn.commit()
     except:
          print("\nInvalid Account Number, Kindly Try Again")

def delete():
     num = int(input("\nEnter your account number to Delete the Data: "))
     try:
          find = 'select cust_acc from customers where cust_acc=?'
          cur.execute(find,(num,))
          match = cur.fetchall()
          
          if num == match[0][0]:
               print("\nBelow are the Details of Account Number : ",num)
          

               details = 'delete from customers where cust_acc=?'

               cur.execute(details,(num,))

               print("\nCustomer Details Deleted Succesfully")
               conn.commit()
     except:
          print("\nInvalid Account Number, Kindly Try Again")

     


     

     

choice ='y'

while (choice=='y'):
     print(a)

     ch = int(input("\nEnter your choice : "))

     if ch==1:
          create()
          
     elif ch==2:
          modify()
          
     elif ch==3:
          deposit()
          
     elif ch==4:
          withdraw()
          
     elif ch==5:
          check()
          
     elif ch==6:
          display()
          
     elif ch==7:
          delete()

     else:
          print("\nInvalid Input, Try Again")
          break

     opt = input("\nDo you want to continue [Y/N]  : ").lower()

     if opt =='y':
          choice='y'
          
     elif opt == 'n':
          choice='n'

     else:
          print("Invalid Input, Kindly Try Again")
     
          
     


#1create()

#2modify()
#3deposit()
#4withdraw()
#5check()
#6display()
#7delete()



conn.close()

