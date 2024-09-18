class Company:
    def __init__(self):
        #private variable
        self.__companyName = "google"

        #public variable
        self.rank = 2

        #protected variable
        self._branchCount = 10

    def display(self):
        print(self.__companyName)

class B(Company):
    pass

c1 = Company()
c1.display()
print(c1.rank)
print(c1._branchCount)

b1 = B()
print(b1._branchCount)

