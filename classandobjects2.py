'''
class Student:
    def __init__(self):
        self.name = "Don"
        self.register_id = "123"

    def display(self):
        print("Name:",self.name)
        print("Reg number:",self.register_id)

s1 = Student()
s2 = Student()

s1.name = "Maddy"
s1.register_id = "001"

s2.name = "Vivek"
s2.register_id = "002"

s1.display()
s2.display()
'''

'''
class Fruit:
    def __init__(self,color):
        self.color = color
    def display(self):
        print(self.color)

f1 = Fruit("Red")
f1.display()
'''

'''
class Teacher:
    def __init__(self,name,regNo):
        self.name = name
        self.regNo = regNo
    def display(self):
        print("Name:",self.name)
        print("Reg Number:",self.regNo)

t1 = Teacher("Angel","001")
t2 = Teacher("Queen","002")

t1.display()
t2.display()
'''

'''
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print("Addition:",self.a + self.b)
    def sub(self):
        print("Subtraction:",self.a - self.b)
    def mul(self):
        print("Multiply:",self.a * self.b)
    def div(self):
        print("Division:",self.a / self.b)

cal1 = Calculator(3,2)
cal1.add()
cal1.sub()
cal1.mul()
cal1.div()
'''

class Calculator:
    def add(self,a,b):
        print("Addition:",a + b)

cal2 = Calculator()
cal2.add(3,4)














