'''
#Polymorphism1 - The following function works similar to java/c++ method overloading
def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)
'''


#Polymorphism2 - Here we are using method overriding
class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal makes a sound")
    

class Dog(Animal):
    def __init__(self):
        pass

    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def __init__(self):
        pass

    def soud(self):
        print("Bird Sing")


obj1 = Dog()
obj1.sound()
