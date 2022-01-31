class Students:
    def __init__(self,Name,Beverages,Subject):#Constructor 
        self.name= Name
        self.beverages = Beverages
        self.sub = Subject
        
Harry = Students('harry','Coldrink','Maths')#Init or constructor method is a way to pass arguments to the Object or instance of the class.

print(Harry.beverages)
print(Harry.name)
print(Harry.sub)