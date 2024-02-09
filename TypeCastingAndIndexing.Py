#Python Program to Practice Typecasting and Indexing
#TypeCasting have two types one is Implicite and second is Explicite

#Implicite TypeCasting
print(1+2+3.0)
print(10/2)

#Explicite TypeCasting
print(int(10/2))
print(complex(10/2))
print(float(10*2))

#Indexing On String

Name = 'Sachin Tendulkar'

print('Length of Name: ', len(Name))
print('Name[0]', Name[0])
print('Name[5]', Name[5])
print('Name[6]', Name[6])
print('Name[15]', Name[15])
print('Name[-1]', Name[-1])
print('Name[-9]', Name[-9])

#print('Name[20]', Name[20]) ##If try to access index beyond avaialble range gives error as IndexError: string index out of range

#Slicing in String using Positive Indexing
print(Name[:])  #Name[startInex:StopIndex]
print('Fetch Sachin from Name: ', Name[0:6])
print('Fetch Sachin from Name: ', Name[:6])
print('Fetch Tendulkar from Name: ', Name[7:])
print('Fetch chin from Name: ', Name[2:6])

#Slicing in String using Negative Indexing
print('Fetch kar from Name: ', Name[-3:])
print('Fetch rak from Name: ', Name[-1:-4:-1])
print('Reverse Name: ', Name[::-1])
print('Fetch Sacin in reverse Name: ', Name[-11::-1])
print('Fetch Sacin in reverse Name: ', Name[:6][::-1])
print('Fetch Sacin in reverse Name: ', Name[5::-1])
print('Fetch Tendulkar in reverse Name: ', Name[:6:-1])
print('Fetch Tendulkar in reverse Name: ', Name[-1:-10:-1])


