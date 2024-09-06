'''
sum = 0
for i in range(1,6):
    sum = sum + i
print(sum)
'''

'''
sum = 0
for i in range(10):
    sum = sum + int(input("Enter a number:"))
print(sum)
'''

'''
#list
sum = 0
list1 = [1,2,3,4,5]
for i in list1:
    sum = sum + i
print(sum)
'''

'''

list2 = []

for i in range(10):
    list2.append(int(input("Enter number"+str(i+1)+":")))
print(list2)

sum = 0
for j in list2:
    sum += j
print("Sum:",sum)
'''

'''
n = int(input())
sum = 0

for i in range(1,n+1):
    print(i)
    sum += i
print("Sum =",sum)
'''

n = int(input())
for i in range (1,n+1):
    print("Number is:"+str(i)+" and cube of the "+str(i)+" is:",i**3)
