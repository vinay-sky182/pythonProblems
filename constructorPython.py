"""  In Python, constructors are special methods used to initialize objects. The constructor method is called __init__()

Basic Constructor
The __init__() method is automatically called when an instance of a class is created. It allows the class to initialize the attributes of the object. """ 

class Car:
        
    def __init__(self, brand, model, price, milage):
        self.brand = brand # These are the class variables
        self.model = model
        self.price = price
        self.milage = milage

    def start_car(self):
        print(self.brand+" car having model as "+self.model+" has started")

    def stop_car(self):
        print(self.brand+" car having model as "+self.model+" has stoped")

    def print_car_details(self):
        print("Brand of the car is: "+self.brand)    
        print("Model of the car is: "+self.model)    
        print("Price of the car is: "+str(self.price))    
        print("Milage of the car is: "+str(self.milage))
        print("----------------------------------------")    


svdi = Car("Maruti", "Swift", 800000, 21) 
svdi.start_car()
svdi.stop_car()
svdi.print_car_details()
hamz = Car("Honda", "Amaze", 900000, 14.5) 
hamz.start_car()
hamz.stop_car() 
hamz.print_car_details()     