class comp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def paid(self):
        print("name:",self.name,"salary:",self.salary)
emp1=comp(input("name:"),input("salary:"))
emp2=comp(input("name:"),input("salary:"))
emp1.paid()
emp2.paid()