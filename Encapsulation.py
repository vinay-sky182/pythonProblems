# Encapsulation - Wrap the data and code within a single unit which known as a class and these variables (private) can not be accessed directly outside class, methods are non-private which can use to performing the operations or modiffing and accessing the variables from outside the class.


class AB:

    __age = 0      # private variable

    def set_age(self, age):
        AB.__age = age

    def get_age(self):
        return AB.__age    



obj = AB()
obj.set_age(14)
print(obj.get_age())

