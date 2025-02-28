class Car:

    wheels = 4

    def __init__(self, brand, model, price, milage):
        self.brand = brand # Instance Variables
        self.model = model
        self.price = price
        self.milage = milage


    def start_car(self):
        print(f"{self.brand} car having model as {self.model} has started")


    @staticmethod
    def print_car_wheels():
        print(Car.wheels)
        c1 = Car("Hyundai", "i10 Nios", 1000000, 13) 
        c1.start_car()    


swift = Car("Maruti Suzuki", "Swift", 800000, 24)  
amaze = Car("Honda", "Amaze", 900000, 14.5)  
swift.start_car()
amaze.start_car()
Car.print_car_wheels()    

# Instance methods and variables belongs to Object memory    
# Static methods and variables belongs to Calss memory   
# To write the static method we need to use '@staticmethod' anotation