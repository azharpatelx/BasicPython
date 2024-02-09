#Program to Practice Methods of String

#To list the methods string support press ''. or use dir('')
#To check detail of every listed method use help(str.nameofthemethod)

#Split:-
#Default split takes space as seperator
# if nothing is given and space is not there then it will print the string as it is 
Name = 'Azhar Imtiyaj Patel'
ip = '198.162.10.109'

print(Name.split())
print(ip.split('.'))
print(ip.split())

#uppercase:-
#Return a copy of the string converted to uppercase.
# str doesnt allow parmenent changes
print(Name.upper())
print('ID of string before modification', id(Name))

Name = Name.upper()
print(Name)
print('ID of string After modification', id(Name))

#titlecase
#Return a version of the string where each word is titlecased.
#More specifically, words start with uppercased characters and all remaining cased characters have lower case.
print(Name.title())

# capitalize : first letter caps only
print(Name.capitalize())

#lowerCase:Return a copy of the string converted to lowercase
print(Name.lower())

#SwapCase: Convert uppercase characters to lowercase and lowercase characters to uppercase
print(Name.swapcase())

#replace: Return a copy with all occurrences of substring old replaced by new.
#replace(old,new)
print(Name)
print(Name.replace('PATEL', 'PATIL'))

#Strip: Return a copy of the string with leading and trailing whitespace remove

Name1 = '   Azhar  '
print(Name1.strip())
print(Name)
print(Name.replace(' ', ''))

Name2 = '###Azhar***'
print(Name2)
print(Name2.strip('#*'))

#Count
Name3 = 'i Love India'

print(Name3.count(' '))
print(Name3.count('i'))
print(Name3.count('INDIA'))
print(Name3.count('India'))

#startswith(): to check either str starts with given object
print(Name3.startswith('i'))
print(Name3.startswith('I'))

# endswith(): to check either str end with given object 
print(Name3.endswith('a'))
print(Name3.endswith('Z'))
print(Name3.endswith('India'))

 # find(): will return an index where particular string /block/char is present
 #Return -1 on failure.
print(Name3.find('i'))
print(Name3.find('India'))
print(Name3.find('z'))

#rfind(): if u want index from right side then use rfind
print(Name3.rfind('i'))

#enumerate: to check index of all elements one by one use enumerate() function
print(list(enumerate(Name3)))
print(tuple(enumerate(Name3)))

# index(): it also returns lowest index
#Raises ValueError when the substring is not found
print(Name3.index('India'))
#print(Name3.index('Z')) ##gives error

#Join(): Concatenate any number of strings.
L1 = ['Azhar', 'IMTIYAJ', 'Patel']
print(''.join(L1))
print(':'.join(L1))

#isalpha, isalnum, isdigit, isspace, All is cases
a = 'teamWork'
b = 'team123'
c = '200'

print(a.isalpha())
print(a.isdigit())
print(b.isalnum())
print(c.isdigit())
print(b.isspace())
print(b.isascii())
print(b.isupper())
print(c.isdecimal())
print(b.isidentifier())
print(a.islower())
print(c.isprintable())
print(a.istitle())

#format():
# S.format(*args, **kwargs) -> str 
# Return a formatted version of S, using substitutions from args and kwargs.
#The substitutions are identified by braces ('{' and '}').

d = 'India Win by {Run} runs'
print(d.format(Run = 100))

#translate(): Replace each character in the string using the given translation table.
MyDict = {111: 97}
Sample = 'Hello World'

print(Sample.translate(MyDict))

MyDict1 = str.maketrans("l", "o")
print(Sample.translate(MyDict1))
