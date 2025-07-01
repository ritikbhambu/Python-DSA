class Details:
    def __init__(self,name,age,salary):
        self.name = name # public variable (everywhere)
        self._age = age # protected variable (in subclass)
        self.__salary = salary # private variable(inside class only)

    def info(self):
        print(f"the name of the person is {self.name}\nthe age of {self.name} is {self._age} and the salary is {self.__salary}")    
    
    def encap_function1(self):   # Public method
        print(f"printing name through public method {self.name}") 
    
    def _encap_function2(self):  # Protected method
        print(f"printing name through protected method {self.name}")
    
    def __encap_function3(self): # Private method
        print(f"printing name through private method {self.name}")

person = Details("Ritik",20,400000) 
print(person.name)
print(person._age) # advised to use protected in subclass only
# print(person.__salary)  # not accisible outside class
person.info()  

person.encap_function1()
person._encap_function2()
# person.__encap_function3() # not accessible