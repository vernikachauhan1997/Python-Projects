class Employee:
    PTOBalance = 30
    
    def __init__(self,Name,Beverages,Subject):#Constructor 
        self.name= Name
        self.beverages = Beverages
        self.sub = Subject
        
    def print_dt(self):
        return f"Employee name is {self.name} and salary is {self.beverages} and subject passed is {self.sub}"
        
    @classmethod                    #ClassMethod
    def func(cls,newPTO):
        cls.PTOBalance = newPTO
    
    @classmethod                    #Alternate Constructor
    def from_fwdlash(cls,string):
        return cls(*string.split(("/")))
    
    @staticmethod
    def ranstr(string):
        print(f'This is my random {string}')
        
class Student(Employee):            #Single inheritance
    no_of_holiday = 12
    
    def __init__(self, Name,salary,Subject, JProgramming):
        self.name= Name
        self.salary = salary
        self.subject = Subject
        self.programming = JProgramming
    
    def print_dt2(self):
        return f"Employee name is {self.name} and salary is {self.salary} and subject passed is {self.subject} and the languages is {self.programming}"
        
Harry = Employee('harry','Coldrink','Maths')
print(Harry.print_dt())

Johnny = Student('johny',777,'fail',['Python','C#','Java']) 
print(Johnny.print_dt2())

print(Johnny.from_fwdlash('Vernika/Chauhan/Vernika/Chauhan'))

