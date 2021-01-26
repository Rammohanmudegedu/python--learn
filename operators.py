#types of operators  #membership operators(in,not in), #identity operators(is, is not), #bitwise operators(&,|)..

#membership operators
a=5
b=6
list1=[2,3,5,7,9]
if (a in list1):
    print("it is correct")
elif (b not in list1):
    print("this is also correct")
else:
    print("this is not correct")

#identity operators
a=20
b=20
if (a is  b):
    print("both are equal")
elif (a is not b):
    print("both are not equal")
else:
    print("both are diffferent")

#bitwise operators
a=8
b=7
#AND formula
c=a&b
print(c)
# OR formual
d=a|b
print(d)
