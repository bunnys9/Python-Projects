import random

mylist = list(map(int, range(100000,1000000)))

OTP = random.choice(mylist)

print(OTP)
