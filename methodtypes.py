class Laptop:
    chargeType = "C-Type"

    def __init__(self):
        self.brand = ""
        self.price = 34

    def setPrice(self,price):#instance method
        self.price = price

    def getPrice(self):#instance method
        print(self.price)

    @classmethod #decorators
    def changeChargeType(cls):#class method
        cls.chargeType = "B-Type"
        print("Charge Type:",cls.chargeType)
        
    @staticmethod
    def info():
        print("This is Laptop class")

HP = Laptop()
HP.setPrice(3000)
HP.getPrice()

Laptop.changeChargeType()

HP.info()
Laptop.info()
