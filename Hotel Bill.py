mylist = [0,['Idly',30],['Bonda',35],['Wada',40],['Puri',25],['Dosa',45]]
head = """
         Bunny Famous Hotel
             Jammikunta
"""
print(head)
print("Welcomes You!!")
a ="""
1.  Idly   =  Rs.30/-
2.  Bonda  =  Rs.35/-
3.  Wada   =  Rs.40/-
4.  Puri   =  Rs.25/-
5.  DOsa   =  Rs.45/-"""

choice = 'yes'
total  = 0

list_selected_food = [] 
list_header         = ['S.No','Items','Nos','MRP','Total'] 
list_items   = []

total_amount = 0
while(choice=='yes'):
    print(a)
    print()
    select_food = int(input("Select your food item : "))
    Nos    = int(input("Enter your quantity   : "))
    bill = mylist[select_food][1]*Nos
    list_selected_food.append(mylist[select_food][0])
    mytup = (mylist[select_food][0],Nos,mylist[select_food][1], bill)
    list_items.extend(mytup)
    total_amount= total_amount+bill
    print()
    print("Your order : ", end="")
    for i in range(len(list_selected_food)):
        print(list_selected_food[i], end="\t")
    print()
    print()

    choice = input("Do you want add items : ")

k=1
l = 0

print()
print()
print()
print()
print()

print("_______________________________________")

print(head)



print("---------------------------------------")
for i in range(len(list_header)):
    print(list_header[i], end ="\t")
print()
print("---------------------------------------")


for i in range(int(len(list_items)/5)+1):
    print(' ',k, end="\t")
    for j in range(4):
        if l<len(list_items):
            print(list_items[l], end='\t')
        l+=1
    print()
    k+=1
print("---------------------------------------")

print(f"  Net Total Amount           Rs.{total_amount}/-")
print("---------------------------------------")
print()
print()
print("     Thank You and Visit Again!!!")
print("_______________________________________")


