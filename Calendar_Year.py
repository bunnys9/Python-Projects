#month      = int(input("Enter your month : "))

list_month = [0, 'January', 'February', 'March', 'April', 'May', 'June','July',
              'August', 'September', 'October', 'November', 'December']

week       = ['Sun', 'Mon','Tue','Wed','Thu','Fri','Sat']

start_days = [0,1,4,5,1,3,6,1,4,0,2,5,0]
month_days = [0, 31,29,31,30,31,30,31,31,30,31,30,31]


for month in range(1,13):
    k=1
    start_day  = 0
    print(f"\n\n{list_month[month]} 2024\n")
    for i in range(len(week)):
        print(week[i], end='\t')
    print()
    for i in range(6):
        for j in range(7):
            if start_day >=start_days[month]:
                if k<=month_days[month]:
                    print(k, end='\t')
                    k+=1
            else:
                print(end="\t")
            start_day+=1
        print()

    
