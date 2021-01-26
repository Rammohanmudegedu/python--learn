import time;
import calendar;
import os
class myprogram:
    def funcprgm(self):
        a,b,c=1,2,3
        if a<b and b<a:
            print("this is wrong")
        elif b>a and c>b:
            print("this is correct")
        elif a>b and b<c:
            print("this is also correct")
        else:
            print("this else")
        print(time.asctime(time.localtime()))
        print(calendar.prcal(1997))
        print(calendar.month(2020,11))

        for i in range(5):
            for j in range (6):
                print((i,j))

        for i in range(10):
            if i==6:
                break
                print("im in for loop")

        a=0
        while True:
            print("im in first while")
            a+=1
            if a==10:
                break


        b=0
        while b<15:
            print("im in second while")
            b+=1

        file=open("e:/ortho.txt","r")
        print(file.read())
        file.close()

obj = myprogram()
obj.funcprgm()


class animal():
    def eat(self):
        print("eating")


class dog(animal):
    def bark(self):
        print("barking")


class babydog(dog):
    def sleep(self):
        print("sleeping")


d=babydog()
d.eat()
d.bark()
d.sleep()

class forleg():
    def eat(self):
        print("eating")


class dog():
    def bark(self):
        print("barking")


class babydog(forleg, dog):
    def sleep(self):
        print("sleeping")


d=babydog()
d.eat()
d.bark()
d.sleep()

class comp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def paid(self):
        print("name:",self.name,"salary:",self.salary)
emp1=comp(input("yourname:"),input("yoursalary"))
emp2=comp(input("yourname:"),input("yoursalary:"))
emp1.paid()
emp2.paid()
