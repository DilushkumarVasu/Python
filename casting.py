a = int("10")#casting
b = int("20")#casting
print (type(a))
print(type(b))
c = a + b
print(c)

"""
please note that while giving usre input using input() function
it obtain the value as a string, so you should cast that given value according to
your requirement
"""

"""
d = int(input())
e = int(input())
f = d + e
print(f)

#Ex - 1
name = input()
age = input()
print("My name is:",name)
print("My age is:",age)

#Ex - 2
address = input()
print("My adress is:",address)

#Ex - 3
num1 = int(input())
num2 = int(input())
num3 = int(input())

multiply = num1 * num2 * num3
add = num1 + num2 + num3
result = multiply / add
print(result)

"""

#Ex - 4
student = input()
score = int(input())
department = input()

print("Student's name is",student)
print("Stuent's score is",score/10,"/10")
print("Student's department is",department)
