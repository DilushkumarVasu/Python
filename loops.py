'''
for i in "apple":
    print(i)

for i in range(5):
    print(i)

for i in range(1,5):
    print(i)
'''

'''
for i in range(1,11):
    print(i,"x 2 =",i*2)
    #print(i*2)
'''

'''
a = int(input("a = "))
b = int(input("b = "))

for i in range(a+1,b):
    print(i)
'''

'''
for i in range(1,11):
    if(i%2==0):
        print(i)
'''

'''
count1 = 0
count2 = 0
for i in range(1,11):
    if(i%2!=0):
        count1 = count1 + 1
    else:
        count2 = count2 + 1
print("Even:",count1)
print("Odd:",count2)

'''

count = 0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count+=1
print(count)

