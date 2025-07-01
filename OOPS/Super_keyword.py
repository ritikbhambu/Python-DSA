class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Call Vehicle's constructor
        self.model = model
        print(f"Car model: {self.model}")

# Create an object
c = Car("Toyota", "Corolla")
