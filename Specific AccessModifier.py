class ParentClass:
    def __init__(self, firstname, lastname):
     self.firstname = firstname #Public attributes
     self.lastname = lastname
     
class Childclass1():
     def __init__(self, firstname, lastname):
        self._firstname = firstname #Protected attributes becuaes of single underscore
        self._lastname = lastname
        
class Childclass2(Childclass1):
     def __init__(self, firstname, lastname):
        self.__firstname = firstname #Private attributes becuaes of single underscore
        self.__lastname = lastname
    
        
    