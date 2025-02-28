# self in python: 
""" 
1.) Represents somthing that belongs to the class
2.) Can be used to acess the variables and methods inside the same class 
3.)Inside the class we have to use self to access the properties and outside the class we have to use object refrence to acess the class properties
4.) self parameter can be renamed
5.) Assigning function parameters to class variables  
6.) It is like 'this' keyword of java """  


class Car:
    wheels = 4 # this the class variable

    def initialization_method(self, brand, model, price, milage):
        self.brand = brand # These are the instance variables
        self.model = model
        self.price = price
        self.milage = milage

    def start_car(self):
        print("Car Started");
        print(self.brand+"car having model as "+self.model+" has started")

    def stop_car(self):
        # print("Car Started");
        print(self.brand+"car having model as "+self.model+" has stoped")
        

    def example_one(self):
        print(self.wheels);
        self.start_car();



# Using object refrence we can access the properties of the class outside the class

car = Car();
car.initialization_method("Honda", "Amaze", 900000, 14.5);
car.example_one();
# print(car.wheels);
# car.start_car();


