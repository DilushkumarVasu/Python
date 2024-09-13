class Grandpa:
    def money(self):
        print("Grandpa's money")

class Dad(Grandpa):
    def phone(self):
        print("Dad's phone")

class Mom:
    def sweet(self):
        print("Mom's sweet")

'''
Multiple inheritance: Python supports multiple inheritance directly,
allowing a class to inherit from more than one class.
Java, however, does not support multiple inheritance of classes
due to ambiguity issues (the "diamond problem").
Instead, Java achieves multiple inheritance through the use of interfaces.
'''        
class Son(Dad,Mom):
    def laptop(self):
        print("Son's laptop")

ram = Son()
ram.laptop()
ram.phone()
ram.sweet()

dada = Dad()
dada.money()

#multi level inheritance used here
ram.money()#here ram can access both dad's and gradnpa's assets



class Father:
    def money(self):
        print("Dad's money")

class Mother:
    def land(self):
        print("Mother's land")

#Single + Multilvel + Hierarchical + Multiple Inheritance = Hybrid Inheritance
class Son1(Father,Mother):
    pass

#Hierarchical Inheritance
class Son2(Father):
    pass

s1 = Son1()
s1.money()
s1.land()

s2 = Son2()
s2.money()



