'''
i = 1
while(i<=5):
    print(i)
    i = i + 1
'''
'''
i = 1
while(i <= 20):
    print(i*10,end=",")
    i = i+1
'''

'''
i = 10
while(i>0):
    print(i)
    i = i - 1
'''

n = int(input("Enter a positive number:"))
fact = 1
while(n > 0):
    fact = fact * n
    n = n - 1
print(fact)
