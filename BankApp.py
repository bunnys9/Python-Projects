""" Banking Application """

# Back-end Process

# Bunny Bank (Sample bank name taken)

import random 
import sqlite3 as sql




"""  Some Variable which are used in the program  """

a = """
     1.  Create Account
     2.  Account Details
     3.  Update Details
     4.  Deposit
     5.  Withdraw
     6.  Delete Account"""


b = """

Enter your Choice number to update the KYC:

1.  Name
2.  Date of Birth
3.  Phone Number
4.  Address
"""


print()
print("-----------------------------")
print("    Welcome to Bunny Bank")
print("-----------------------------")





#Generating random numbers from 1000 to 9999, which are assigned to Customer Account numbers

def Accn_Num():
     mylist_accn_num = list(map(int, range(1000,10000,7)))
     accn_num = random.choice(mylist_accn_num)
     cust_accn_list = []

     if accn_num not in cust_accn_list:
          cust_accn_list.append(accn_num)
          return accn_num
               
     else:
          Accn_Num()






          
#Function Reusing in the program
          
def Display(accn_num):
     data = 'select * from customers where cust_acc = ?'
     cur.execute(data,(accn_num,))

     res = cur.fetchall()

     print()
     print("Account Number : ",res[0][0])
     print("Name           : ",res[0][1])
     print("Date of Birth  : ",res[0][2])
     print("Phone Number   : ",res[0][3])
     print("Address        : ",res[0][4])
     print(f"Balance        :  Rs.{res[0][5]}/-")






# Creating Database name'BankUsers'

conn = sql.connect("BankUsers.db")     #Connection Establised
cur  = conn.cursor()






# Creating New Customer by reading input from the enduser
def Create_Account():
     
     table = 'create table if not exists customers(cust_acc int primary key, name text, dob date, ph int(10), address text, bal int)'
     cur.execute(table)
     
     data = 'insert into customers values(?, ?, ?, ?, ?, ?)'
     
     cust_acc  = Accn_Num()
     cust_name = input("Enter your Name          : ")
     cust_dob  = input("Enter your Date of Birth : ")
     cust_phno = input("Enter your Mobile Number : ")
     cust_add  = input("Enter your Address       : ")
     bal = 0

     cur.execute(data,(cust_acc, cust_name, cust_dob, cust_phno, cust_add, bal))
     conn.commit()

     print("\nBelow are the Details created for ",cust_name)
     Display(cust_acc)







# Displaying the Customer Details with the help of account number details(reading data from the enduser)

def Display_Details():

     
     accn_num = int(input("Enter your Account Number : "))
     data = 'select * from customers'
     res = cur.execute(data)
     num = res.fetchall()
     mylist = []

     for i in num:
          mylist.append(i[0])


     if accn_num in mylist:
          Display(accn_num)

     else:
          print("Account not found, Kindly Register")            #if account number not found it will through the message





# Updating the Customer Details with the help of account number details(reading data from the enduser)

def Update_Details():
     
     accn_num = int(input("Enter your Account Number : "))
     data = 'select * from customers'
     cur.execute(data)

     num = cur.fetchall()

     mylist = []

     for i in num:
          mylist.append(i[0])
     

     if accn_num in mylist:
          
          print("\nBelow are the Details of Account Number : ",accn_num)                        
          Display(accn_num)
               
          print()
          print(b)
          
          ch = int(input("Enter your Option : "))
          
          if ch==1:
               name = input("Enter Updated Name : ").capitalize()
               details = 'update customers set name = ? where cust_acc = ?'
               cur.execute(details,(name,accn_num))
               conn.commit()

               print("\nBelow are the Updated Details of Account Number : ",accn_num)
               Display(accn_num)
               
          elif ch==2:
               dob = input("Enter Updated DOB : ")
               details = 'update customers set dob = ? where cust_acc = ?'
               cur.execute(details,(dob,accn_num))
               conn.commit()

               print("\nBelow are the Updated Details of Account Number : ",accn_num)
               Display(accn_num)
               
          elif ch==3:
               phno = input("Enter Updated Phone Number : ")
               details = 'update customers set ph = ? where cust_acc = ?'
               cur.execute(details,(phno,accn_num))
               conn.commit()

               print("\nBelow are the Updated Details of Account Number : ",accn_num)
               Display(accn_num)
               
          elif ch==4:
               add = input("Enter Updated Address : ")
               details = 'update customers set address = ? where cust_acc = ?'
               cur.execute(details,(add,accn_num))
               conn.commit()

               print("\nBelow are the Updated Details of Account Number : ",accn_num)
               Display(accn_num)
               
     else:
          print("Account not found, Kindly Register")            #if account number not found it will through the message







# Crediting the amount in the Customer Account with the help of account number details(reading data from the enduser)

def Deposit_Details():
     
     accn_num = int(input("Enter your Account Number : "))
     data = 'select * from customers'
     cur.execute(data)

     num = cur.fetchall()
     mylist = []

     for i in num:
          mylist.append(i[0])
     

     if accn_num in mylist:

          print("\nBelow are the Details of Account Number : ",accn_num)              
          Display(accn_num)

          amount = int(input("How much do you want to deposit : "))
               
          details = 'update customers set bal = bal+? where cust_acc = ?'
          cur.execute(details,(amount,accn_num))
          conn.commit()
               
          print("\nBelow are the Updated Details of Account Number : ",accn_num)
          Display(accn_num)

     else:
          print("Account not found, Kindly Register")            #if account number not found it will through the message







# Withdrawing amount from the Customer Account with the help of account number details(reading data from the enduser)        

def Withdraw_Details():
      
     accn_num = int(input("Enter your Account Number : "))
     data = 'select * from customers'
     cur.execute(data)

     num = cur.fetchall()

     mylist = []

     for i in num:
          mylist.append(i[0])
     

     if accn_num in mylist:
          print("\nBelow are the Details of Account Number : ",accn_num) 
          Display(accn_num)

          amount = int(input("How much do you want to Withdraw : "))

          details = 'select * from customers where cust_acc = ?'
          cur.execute(details,(accn_num,))
          res = cur.fetchall()
                   

          #it is executed if withdraw amount is lesser than the balance
          
          if res[0][5]>=amount:  
               
               detail = 'update customers set bal = bal-? where cust_acc = ?'

               cur.execute(detail,(amount,accn_num))
               conn.commit()
                      
               print("\nBelow are the Updated Details of Account Number : ",accn_num)
               Display(accn_num)

          
                   

          #it is executed if withdraw amount is greater than the balance          
          else:
               print("\nInsufficent Funds")
                   


     else:
          print("Account not found, Kindly Register")    #if account number not found it will through the message

     




# Deleting the Customer Accounts Details with the help of Customer Account Details( Reading data from enduser)

def Delete_Account():
     accn_num = int(input("Enter your Account Number : "))
     data = 'select * from customers'
     cur.execute(data)

     num = cur.fetchall()

     mylist = []

     for i in num:
          mylist.append(i[0])
     

     if accn_num in mylist:
          print("\nBelow are the Details of Account Number : ",accn_num)                       
          Display(accn_num)

          details = 'delete from customers where cust_acc=?'

          cur.execute(details,(accn_num,))

          print("\nCustomer Details Deleted Succesfully")
          conn.commit()
          
     else:
          print("Account not found, Kindly Register")      #if account number not found it will through the message
     


choice = 'yes'



"""
Below is the Control Flow of the Program by selecting the appropriate options

1. Create_Account()
2. Display_Details()
3. Update_Details()
4. Deposit_Details()
5. Withdraw_Details()          
6. Delete_Account()

"""




while(choice=='yes'):
     print(a)
     ch = int(input("\nEnter your choice : "))

     if ch==1:
          Create_Account()
          
     elif ch==2:
          Display_Details()
          
     elif ch==3:
          Update_Details()
          
     elif ch==4:
          Deposit_Details()
          
     elif ch==5:
          Withdraw_Details()
          
     elif ch==6:
          Delete_Account()

     else:
          print("\nInvalid Input, Try Again")
          break

     opt = input("\nDo you want to continue [Y/N]  : ").lower()

     if opt =='y':
          choice='yes'
          
     elif opt == 'n':
          choice='no'

     else:
          print("Invalid Input, Kindly Try Again")
     
          
 

conn.close()   # Connection Closed




print()
print("-----------------------------")
print("         Thank You!! ")
print("-----------------------------")
    
          
     
