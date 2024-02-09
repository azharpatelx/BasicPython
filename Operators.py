##Python Program for Practicing Operators

a = 10
b = 20
c = [1,2,3,4,5]
d = 0
Place = 'pune'
NativePlace = 'pune'
name = 'azhar'

#Assignment Operator
e = 100
print('e= ',e)

#Aritmatic Operators
print('a+b = ', a+b)
print('b-a = ', b-a)
print('a*b = ', a*b)
print('b/a = ', b/a)
print('b//a = ', b//a)
print('a**b = ', a**b)

#Comparison Operator
print('a > b: ', a > b)
print('a < b: ', a < b)
print('a >= b: ', a >= b)
print('a <= b: ', a <= b)
print('Place == name: ', Place == name)
print('Place != name: ', Place != name)

#Membership Operator
print('1 in c: ', 1 in c)
print('10 in c: ', 10 in c)
print('u in place: ', 'u' in Place)
print('R in place: ', 'R' in Place)

#Identity Operator
print('a is b: ', a is b)
print('a is not b: ', a is not b)
print('ID:Address in memory location of a is: ', id(a))
print('ID:Address in memory location of b is: ', id(b))
print('Place is NativePlace: ', Place is NativePlace)
print('ID:Address in memory location of Place is: ', id(Place))
print('ID:Address in memory location of NativePlace is: ', id(NativePlace))

#Logical Operator
print('name == azhar and place == pune: ', name == 'azhar' and Place == 'pune')
print('name == azhar and place == Mumbai: ', name == 'azhar' and Place == 'Mumbai')

print('name == azhar or place == pune: ', name == 'azhar' or Place == 'pune')
print('name == azhar or place == Mumbai: ', name == 'azhar' or Place == 'Mumbai')
print('name == patel or place == Mumbai: ', name == 'patel' or Place == 'Mumbai')

print('not of a', not a)
print('not of d', not d)
