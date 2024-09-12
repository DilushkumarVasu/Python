'''
class goa:
    name = ""
    drink = ""
    def party(self):
        print("Party")
    def beach(self):
        print("Beach")


ramesh = goa() #object
suresh = goa() #object

ramesh.name = "Ramesh"
suresh.name = "Suresh"

ramesh.drink = "Yes"
suresh.drink = "No"

print(ramesh.name)
print(suresh.name)
'''

'''
class laptop:
    price = 0
    processor = ""
    ram = ""

HP = laptop()
DELL = laptop()
LENOVO = laptop()

HP.price = 50000
HP.processor ="i5"
HP.ram = "8GB"

DELL.price = 60000
DELL.processor = "i7"
DELL.ram = "16GB"

print(HP.price)
print(DELL.price)
'''

class laptop:
    #constructor
    def __init__(self):
        self.price = 0
        self.ram = ""
        self.proc = ""
    
    def display(self):
        print("Price:",self.price)
        print("Ram:",self.ram)
        print("proc:",self.proc)

    '''
    1)pass is used as a placeholder in Python where code is syntactically required
    but no action is needed.
    2)It helps you avoid syntax errors when leaving blocks
    of code empty during development.
    3)Code Under Development: When you're developing code but
    haven't implemented certain parts yet, you can use pass to
    create the structure and fill in the logic later.
    4)For Readability: It can also be used when you're planning
    out the code and want to indicate that something will go here later.
    '''
    def testing():
        pass

HP = laptop()
HP.price = 50000
HP.ram = "8GB"
HP.proc = "i5"
print(HP.price)

HP.display()

#DEL = laptop(2000,"i8","32GB")



















