""" class A:
    __a = 5

    def __sample(self):
        print("Inside sample method of Class A")


    def print_details(self):
        print(self.__a)
        self.__sample()    


obj = A()
obj.print_details()    """        



# Getter and Setter methods with private variables 

class AB:

    __age = 0

    def set_age(self, age):
        AB.__age = age

    def get_age(self):
        return AB.__age    



obj = AB()
obj.set_age(14)
print(obj.get_age())

