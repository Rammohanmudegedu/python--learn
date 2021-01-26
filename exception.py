import math
num=int(input("user input:"))
try:
    res=math.factorial(num)
    print(res)
except:
    print("please enter valid number")
