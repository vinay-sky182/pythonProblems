class A:
    a = 5

    def sample(self):
        print ("Inside sample method of class A")


class B(A):
    a = 10

    def sample(self):
        print("Inside sample method of class B") 

    def print_properties(self):
        print(self.a)
        self.sample()
        print(super().a)
        super().sample()


obj = B()    
obj.print_properties()               


class AB:
    def __init__(self):
        print("Inside __init__ method of Class AB")


class BC(AB):
    pass

