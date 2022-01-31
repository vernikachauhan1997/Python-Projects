#Map Function
#variable = list(map(function, iterableobject))

number = int(input('Enter the number:-'))
num = []
num.append(number)

def addition(number):
    return number*number

result = list(map(addition,num))
print(result)

#OR
result1= list(map(lambda x:x*x,num))
print(result1)

print('-----------------------------------------------------')

#Filter function
#variable = list(filter(function,sequence))

evennum = [1,2,3,4,5,6,7,8,9]

def func(evennum):
    return evennum%2 == 0

result1 = list(filter(func,evennum))
print(result1)
print('-----------------------------------------------------')

#Reduce Function
from functools import reduce

result2 = reduce(lambda x,y:x+y,evennum)
print(result2)