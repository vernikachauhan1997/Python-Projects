students_name = ['Vernika', 'Kartika','Rohan','Basu']
d1 = {'Vernika':'Samosa', 'Kartika':'Dosa','Arjun':'Momos'}
reason = "Below are the list of students:-"

def function(*args):#Exmaple of args
    for items in args:
        print(items)
        
def function_normal(normal,*args):#Exmaple of Normal with other args 
    print(reason)
    for items in args:
        print(items)
       
def function_Kwards(normal,*args,**kwargs):#Exmaple of kwargs,args and Normal 
    print(reason)
    for items in args:
        print(items)
    for key, value in kwargs.items():
        print( key ,value)
       
#Calling functions
function(*students_name)
function_normal(reason,*students_name)
function_Kwards(reason,*students_name,d1)

#Order of the arguments is :Normal argu, *args,**kwards...these are just convention to represnt, the names can be different too.