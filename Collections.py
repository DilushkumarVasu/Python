#Collections/Arrays in Python


#List
'''
can add duplicate element,
can store any data type,
can modify the element
'''
a = [1,2,3,4,5]
print(a)
a.append(6)#append
a.append(10)
a.append("test")
a.append(10)
print(a)
a.insert(1,20)#insert
print(a)
print(a[2])
a[1] = 30 #replace
print(a)
a.pop(4)#remove
print(a)
a.pop()#remove the last element
print(a)

list1 = [1,2,3,4,5,6]
list2 = [10,20,30]
list1.extend(list2)
print(list1)

#tuple
'''
can add duplicate element,
can store any data type,
can't modify the element-->(add,remove,replace/update)
but we can cast it to list item
'''
tuple1 = (1,2,3,4,5)
print(tuple1)

testList = list(tuple1)
print(testList)

#set
'''
can't add duplicate element,
any type of data can be stored,
can't modify the element, but can add or remove elements
here you can update the set by adding two sets like that using update()
'''

set1 = {1,2,3,4,4}
print(set1)
set1.add(10)
print(set1)
set1.remove(4)
print(set1)
set1.pop()#sets are unordered, hence this will print different output each time
print(set1)

#Dictionary
'''
do not allow duplicate value
any type can be stored
'''

diction1 = {
    "name":"Admin",
    "age":1,
    "location":"Wattala",
    "subjects":["a","b","c"]
    }
print(diction1)
print(diction1["name"])
print(diction1.keys())
print(diction1.values())

diction1["age"]=2
print(diction1)

diction1.update({"age":3})
print(diction1)

diction1["sport"]="spt1"
print(diction1)

diction1.pop("age")
print(diction1)

del diction1["sport"]
print(diction1)

diction1.clear()
print(diction1)


