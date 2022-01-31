import re
import math
# from math import floor
# import string


# listA = [1,2,3,4,5,6]

# def func(listA):
#      return listA*listA
 
# # var = list(map(func,listA))
# # print(var)

# # var = list(map(lambda x:x**2,listA))
# # print(var)

# Neg_um = [-1,-2,-3,-4,0,1,2]
# float_num = [1,2,3,4,5,6]
# String = ["My", "name", "is", "Vernika" ,"Chauhan"]
# result = list(map(abs,Neg_um))
# print(result)

# result1 = list(map(float,Neg_um))
# print(result1)

# result2 = list(map(str,Neg_um))
# print(result2)

# result3 = list(map(floor,Neg_um))
# print(result3)

# result4 = list(map(len,String))
# print(result4)

# result5 = list(map(pow,Neg_um,float_num))
# print(result5)

# s = ["vernika...",".....chauhan"]
# # result5 = list(map(lambda s: s.split("."),s))
# # print(result5)

# def removepunc(s):
#     return re.sub(r'[!?@#$%^.\|]',"",s)

# res = list(map(removepunc,s))
# print(res)

# print(ord("V"))
# print(chr(10))

# res = "".join(map(slice[:-1],"My name is Vernika Chauhan"))
# print(res)

# numbers = [1,2,3,4,5,6,9,67,78,9]

# def prime_num(i):
#     return i%i ==0

# even = list(filter(prime_num,numbers))
# print(even)

numbers = [0,2,4,6,8,-7,-5,-3,-1]

# def is_pos(num):
#     return num>=0

# out = list(map(math.sqrt ,filter(is_pos,numbers)))
# print(out)

from functools import reduce

result2 = reduce(lambda x,y:x+y,numbers)
print(result2)
        
        

        
        
    
 
 

