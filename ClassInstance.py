class Employee:
    leavesBalanace = 360           #Class variables
    lastname = 'Singhania'         #Class variables
    
Ramu = Employee() #Instance of  class or Object
Kalu = Employee() #Instance of  class or Object

Ramu.subject = 'Mathmatics' #Instance variable

Kalu.subject = 'Science' #Instance variable

# print(Ramu.leavesBalanace)
# print(Kalu.lastname)

Ramu.leavesBalanace =  490
print(Employee.leavesBalanace)

Employee.leavesBalanace =  495
print(Employee.leavesBalanace)