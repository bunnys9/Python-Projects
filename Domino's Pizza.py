### Pizza Hut



#Header Section Starts here
def mainhead():

    print("_______________________________________________")
    header ="""
                    Welcome to
                Domino's  Pizza
                    Kukatpally"""
    print(header)
    print("-----------------------------------------------")
mainhead()


print()
print()
print("Menu Items are below : ")
#Customer order details

order = """
1.  Peppy Panner    =  Rs.459
2.  Golden Corn     =  Rs.89
3.  Veg-Pizza       =  Rs.99
4.  Non-Veg Pizza   =  Rs.149
5.  Cheesy          =  Rs.109
6.  Spiced Chicken  =  Rs.559
7.  Indi Chicken    =  Rs.599
8.  Chicken Sauce   =  Rs.369
9.  Cheese Corn     =  Rs.379
10. Mexican         =  Rs.469
"""


list_order = [0,['Peppy Panner',459],['Golden Corn',89],['Veg-Pizza',99],
['Non-Veg Pizza',149],['Cheesy',109],['Spiced Chicken',559],
['Indi Chicken',599],['Chicken Sauce',369],['Cheese Corn',379],
['Mexican',469]]


choice ='yes'

selected_item = []
final_item    = []
final_amount   = 0
head = ['S.no', 'Item Name', 'MRP', 'Nos', 'Total']
def header():
    for i in range(len(head)):
        print(head[i], end='\t')
    print()

while(choice=='yes'):
    print(order)
    select = int(input("\nSelect your Item s.no : "))
    nos    = int(input("Enter your Quantity   : "))

    bill   = list_order[select][1]*nos
    mytup  = (list_order[select][0], list_order[select][1], nos, bill)
    final_amount = final_amount+bill
    final_item.extend(mytup)
    add    = input("Do you want to modify[y/n] : ")
    print()
    if add == 'y':
        header()
        k=1
        s=0
        for i in range(int(len(final_item)/4)):
            print(' ',k, end="\t")
            for j in range(4):
                if s<len(final_item):
                    print(final_item[s], end="\t")
                    s+=1
            print()
            k+=1
        mod = int(input("Enter Order no to Delete: "))
        remove = final_item[((mod-1)*4)+3]
        print(remove)
        for i in range(4):
            final_item.pop(((mod-1)*4))
        
        final_amount = final_amount-remove
        print()
        print()
        print("Updated Order items : ")
        print("----------------------")
        header()
        k=1
        s=0
        for i in range(int(len(final_item)/4)):
            print(' ',k, end="\t")
            for j in range(4):
                if s<len(final_item):
                    print(final_item[s], end="\t")
                    s+=1
            print()
            k+=1
            
        
        
    
    

    choice = input("\nDo you want to add items: ")
print()
print()
print()
print()
print()
print()
mainhead()

header()
print("-----------------------------------------------")
k=1
s=0
for i in range(int(len(final_item)/5)+1):
    print(' ',k, end="\t")
    for j in range(4):
        if s<len(final_item):
            print(final_item[s], end="\t")
            s+=1
    print()
    k+=1

print("-----------------------------------------------")
print(f"     Net Amount Bill                 Rs.{final_amount}/-")
print("-----------------------------------------------")

print("          Thank You and Visit Again!!!")
print("_______________________________________________")
    
    

   
        












        
    


