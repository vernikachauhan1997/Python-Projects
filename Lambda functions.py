q = (lambda x : x*2)
print(q(10))

e = lambda x,y: x+y
print( e(12,24))

Fruits = ['Apple', 'Banana',  'Orange','Kiwi']
Fruits.sort() # sorting in ascending order
print(Fruits)

Fruits.sort(reverse=True)#Sorting in descending order.
print(Fruits)

list_num = [[2,4,6], [6,8,2],[34,65,4],[4,2,2]]
def sort_userchoice(var):
    return var[0]
    
list_num.sort(key=sort_userchoice,reverse=True)#reverse=True will make sorting in descending order.var in sort_userchoice function representing list_num
print(list_num)

#OR using lambda functions
list_num.sort(key=lambda var: var[2], reverse=True)
print(list_num)


