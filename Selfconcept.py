class Employee:
    leavesBalanace = 360           #Class variables
    lastname = 'Singhania'         #Class variables
    
    def func1(self):
        return f'Ramu subject is {self.subject}'
    
    def func2(self):
        return f'Kalu subject is {self.subject}'
    
Ramu = Employee() #Instance of  class or Object
Kalu = Employee() #Instance of  class or Object

Ramu.subject = 'Mathmatics' #Instance variable
Kalu.subject = 'Science' #Instance variable

print(Ramu.func1())
print(Kalu.func2())