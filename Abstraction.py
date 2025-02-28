# Abstraction in Python - Abstract Classes (Partial Implimentation) and Abstract Methods

# Abstract Methods : - Methods which have the only declaration with out any definition (implementations / method body)

#  Abstract Classes :- A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. Python provides the **ABC** module to use the abstraction in the Python program. Abstract method need to be declare under **@abstractmethod** annotation.

#  pass simply does nothing, while continue goes on with the next loop iteration.

# If if a child class does not implement all the abstract methods of its parent abstract class, the child class will behave as an abstract class. This is because the child class is still incomplete and cannot be instantiated. Constructors can be created inside of Abstract class.

from abc import ABC, abstractmethod


class A(ABC):

    def __init__(self, a):
        self.a = a


    @abstractmethod
    def method_one(self):
        pass


    @abstractmethod
    def method_two(self):
        pass


    def method_three(self):
        print("Inside method_three", self.a)

    
class B(A):

    def method_one(self):
        print("Inside method_one")


    def method_two(self): 
        print("Inside method_two") 


obj = B(3)
obj.method_one()
obj.method_two()
obj.method_three()
