#Python Program to Practice List, Set and Dict

a = [1,2,3,4,5,6]

#pop():  Remove and return item at index (default last).Raises IndexError if list is empty or index is out of range.
#Pop is index based removal
print(a)

a.pop()
print(a)

a.pop(1)
print(a)

#Assignmnet: Try with -ve index
a.pop(-2)
print(a)

#remove(): Remove first occurrence of value.Raises ValueError if the value is not present.
#we cant keep remove()
a.remove(3)
print(a)

#reverse(): reverse list inplace: # inplace means parmenant
b = [3,1,7,2,9]
print(b)
b.reverse()
print(b)

#sort(): used to sort list inplace. default sorting is in ascending order
# if we want in descending order then user reverse=True
# We cant apply sort over hetro. data
c = [3,1,7,2,9]
b.sort()
print(b)

print('c= ', c)
c.sort(reverse=True)
print('c= ', c)

# sorting will be a-z
 # first it take Cap letters n then small case letters
nm = ['pooja','siddhesh','avinash','aditi','Uma']
print(nm)

nm.sort()
print(nm)

nj = ['pooja','siddhesh','avinash','aditi','uma']
print(nj)
nj.sort()
print(nj)

# sort(key:function,reverse:bool)
print(nm)
nm.sort(key=len)
print(nm)
nm.sort(key=len,reverse=True)
print(nm)

#Set():
#Syntax: {}
#Set doesn't allow duplicates
# Background data structure is Hash Table
# Property of the hash is table does nt preserves sequence
# EEven duplicates are not allowed
# its not like what array does
# In set we dont have indexing , slicing
# Homo/Hetro values allowed
# It is Mutable in nature

d = {1,1,1,2,3,4,4,5,6,6}
print(d)

# Sequence order nt get preserved
e = {'python',0,9,5,'java',-1}
print(e)

#Add(): If the element already exists, the add() method does not add the element.
e.add('Azhar')
print(e)

e.add(100)
print(e)


#pop(): Remove and return an arbitrary set element.
e.pop()
print(e)

#remove: Remove an element from a set; it must be a member.
e.remove('java')
print(e)

#Discard: Remove an element from a set if it is a member. If the element is not a member, do nothing.
e.discard('TITAN')
print(e)
e.discard(-1)
print(e)

# SET OPERATION
d1 = {'A','B','C'}
d2 = {'A','B','D','E'}

# Intersetion: returns common elements
print(d1.intersection(d2))
print(d1)

# union: returns elements from both the set without duplicates
print(d1.union(d2))

# difference: returns uncommon element from set 1
print(d1.difference(d2))

# symmetric_difference: uncommon element from both the sets
print(d1.symmetric_difference(d2))

#Update:Update a set with the union of itself and others
A1={1,2,3}
A2={3,4,5}
A1.update(A2)
print(A1)

#difference_update:Remove all elements of another set from this set.
A1={1,2,3}
A2={3,4,5}
A1.difference_update(A2)
print(A1)

#symmetric_difference_update:Update a set with the symmetric difference of itself and another.
A1={1,2,3}
A2={3,4,5}
A1.symmetric_difference_update(A2)
print(A1)

#intersection_update: Update a set with the intersection of itself and another
A1={1,2,3}
A2={3,4,5}
A1.intersection_update(A2)
print(A1)
