'''
#Type of exceptions
printt("Hi")#compile time/syntax error

#logical error
a = 1
b = 2
print("Addtion of a,b:",a+a)#logical error-actual objctive is missing--->a+b


#runtime error
c = int(input())#value -> 10
d = int(input())#value -> "Hi"
print(c+d)#run time error->invalid literal for int()
'''

#Exception Handling
'''
try:
    c = int(input())
    d = int(input())
    print(c+d)

    d = input()
    e = input()
    print(d/e)
except Exception as e:
    print("Exception message:",e)
'''


try:
    num1 = int(input())
    num2 = int(input())
    txt = input()
    #print(num1/txt)
    print(d)
except ValueError as e:
    print("Value Error:",e)
except TypeError as e:
    print("Type Error:",e)
except Exception as e:
    print("Something wrong")
finally:
    print("Done")
