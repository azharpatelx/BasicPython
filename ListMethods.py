#Python Program to Practice List Methods
#Syntax: []
# list is mutable, Background data structure is array, it can have duplicate records, +ve & -ve indexing supported, slicing also possible, it preserves sequence order 
# List accept homo and hetro data
#+ve and -ve Indexing
L = [100,200,300,400,500]

print('L[0]', L[0])
print('L[1]', L[-1])
print('L[-3]', L[-3])

#Slicing
print(L)
print(L[:])
print(L[2:])
print(L[:3])
print(L[::-1])
print(L[-4:-2])
print(L[-3::1])
print(L[-3::-1])

#Modifying the List
print(L)
L[-1] = 600
print(L)
L[0] = 'azhar'
print(L)
L.append('patel')
print(L)
L.append([1,2,3])
print(L)
L.extend([4,5,6])
print(L)

t = []
t.append('azhar')
print(t)
t.extend('patel')
print(t)
t.append(['a','b','c'])
print(t)
t.clear()
print(t)

# copy(): which gives a shallow copy
#Shallow copy means : just copy the contents and create a new object
a1 = [1,2,3,4,5]
print('ID of a1: ', id(a1))

a2 = a1.copy()
print('a1', a1)
print('a2', a2)
print('ID of a2: ', id(a2))

# Deep Copy: Copy the contents and address wil be same no new object will be created

a3 = a2
print('ID of a3: ', id(a3))

#Assignment
#insert(): add element at specific index
#object will be addedd before given index and only one element can be inserted at a time
print('a1= ', a1)
a1.insert(3,'python')
print('a1= ', a1)
a1.insert(0,'java')
print('a1= ', a1)
a1.insert(7,'azhar')
print('a1= ', a1)
