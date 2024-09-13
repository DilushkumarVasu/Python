class Phone:
    chargeType = "C-Type" #class variable
    def __init__(self,brand,price):
        self.brand = brand #instance variable
        self.price = price #isntance variable
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("ChargeType:",self.chargeType)


samsung = Phone("Samsung",50000)
samsung.display()

redmi = Phone("RedMI",40000)
redmi.display()

Phone.chargeType = "B-Type"
samsung.display()
redmi.display()
print(Phone.chargeType)
print(samsung.chargeType)
