#Q1
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        pass

    def area(self):
        areares = self.length * self.width
        return areares

obj1 = Rectangle(10,4)
print(obj1.area())


#Q2
class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print("Student's Name:",self.name)
        print("Stuent's Grade:",self.grade)

stu1 = Student("AK","A")
stu1.display()

#Q3
class Vehicle:
    def __init__(self):
        pass

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("Car Started")

vh1 = Car()
vh1.start()

#Q4
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        print(self.name,self.salary,self.department)

emp1 = Manager("Mg1",100000,"IT")
emp1.display()
    

