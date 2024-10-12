### Pizza Hut

#Header Section Starts here
print("__________________________")
header ="""
        Welcome to
      Domino's  Pizza
        Kukatpally
"""
print(header)


#Order Details
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

choice = 'yes'

list_order = [0,['Peppy Panner',459],['Golden Corn',89],['Veg-Pizza',99],
['Non-Veg Pizza',149],['Cheesy',109],['Spiced Chicken',559],
['Indi Chicken',599],['Chicken Sauce',369],['Cheese Corn',379],
['Mexican',469]]

bill_amount=0

list_selected   = []
list_bill_items = []

while(choice=='yes'):
    print(order)

    select = int(input("Enter your order no : "))
    nos    = int(input("Quantity : "))
    bill   = list_order[select][1]*nos
    bill_amount = bill_amount+nos
    mytup  =  (list_order[select][0], list_order[select][1], nos, bill)
    list_bill_items.extend(mytup)
    list_selected.append(list_order[select][0])

    print("Your Ordered Items : ", end="")
    for i in range(len(list_selected)):
        print(list_selected[i], end="")
        if i<(len(list_selected)-1):
            print(',', end=" ")
    print()
    print()
    modify = input("If you want to Modify your items[y/n] : ")
    if modify =='y':
        print("Your Ordered Items : ")
        print("---------------------")
        k=1
        for i in range(len(list_selected)):
            print(k,"  ", list_selected[i], end="")
            print(list_selected)
            print()
            k+=1
        print()
        num = int(input("Enter your choice : "))
        list_selected.pop(num-1)
        print("Updated Ordered Items: ")
        if len(list_selected)==0:
            print("Yet to add Items")
        else:
            k=1
            for i in range(len(list_selected)):
                print(k,"  ", list_selected[i], end="")
                print()
                k+=1
            print()
            print()   
        ch = input("Do you want to add items[yes/no]   : ").lower()
        if ch!='yes':
            print("kindly Enter 'Yes' or 'No'")
            break
        else:
            choice==ch

    elif modify=='n':
        ch = input("Do you want to add items[yes/no]   : ").lower()
        if ch!='yes':
            print("kindly Enter 'Yes' or 'No'")
            break
        else:
            choice==ch
    

print(list_bill_items)


    
