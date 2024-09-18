'''
f1 = open("Testing.txt")#read mode by default
content = f1.read()
print(content)
f1.close()

f2 = open("Testing.txt","w")#write mode
f2.write("Ruby \n")
f2.write("Kotlin \n")
f2.close()

f3 = open("Testing.txt","r+")#read write mode
print(f3.read())
f3.close()
'''

f4 = open("Testing.txt","a")#append mode
f4.write("React")
f4.close()
