class Student:
    PTOBalance = 30
    
    def __init__(self,Name,Beverages,Subject):#Constructor 
        self.name= Name
        self.beverages = Beverages
        self.sub = Subject
        
    @classmethod                    #ClassMethod
    def func(cls,newPTO):
        cls.PTOBalance = newPTO
    
    @classmethod              #Alternate Constructor
    def from_fwdlash(cls,string):
        return cls(*string.split(("/")))
    
    @staticmethod
    def ranstr(string):
        print(f'This is my random {string}')
        
Harry = Student('harry','Coldrink','Maths')#Init or constructor method is a way to pass arguments to the Object or instance of the class.
    
Karan = Student.from_fwdlash("karan/45/Science")  

karan = Student('Orange','Pomogranate','Kiwi')  
    
# Harry.newPTO(25)
# print(Harry.PTOBalance)

Karan.ranstr('Pinki')       #Here we are calling staticmethod of class using class instance/Object like Harry, Karan, etc..
Student.ranstr('Shalu')    #Here we are calling static method of class using class name

Student.ranstr.__dict__

