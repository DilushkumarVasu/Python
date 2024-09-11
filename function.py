'''
def add():
    print("Addition Operation")
    a = int(input("Enter a number a:"))
    b = int(input("Enter a number b:"))
    print(a+b)

#You can't call the sub() function hear because you haven't define a sub() function yet
#sub()

def sub():
    print("Subtraction Operation")
    a = int(input("Enter a number a:"))
    b = int(input("Enter a number b:"))
    print(a-b)

add()
sub()

def findevenorodd(num1):
    #num1 = int(input("Enter an integer number:"))
    if(num1 % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def findpassorfail():
    score = int(input("Enter the score:"))
    print("Pass") if score >= 50 else print("Fail")

def printrange(a,b):
    for i in range(a,b+1):
        print(i)
    

findevenorodd(int(input("Enter an integer number:")))
findpassorfail()
printrange(10,20)
'''


def validate(uname,password):
    if(uname == "EMC" and password == "123"):
        return True
    else:
        return False

s_username = input("Enter the username:")
s_password = input("Enter the password:")
validation_result = validate(s_username,s_password)
print(validation_result)

def cal(a,b,c):
    return (a+b)*c

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print(cal(a,b,c))
    
    









































    
