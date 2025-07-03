from abc import ABC , abstractmethod #imported to use @abstractmethod
class vehicle(ABC): # vehicle is an abstract clas
    @abstractmethod
    def start(self): # abstract method
        pass

class car(vehicle): # inheriting abstract class
    def start(self): # implementing abstract method
        print("engine is started")       

car_obj = car()
car_obj.start()        