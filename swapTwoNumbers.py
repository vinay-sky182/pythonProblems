# class SwapTwo_Numbers:


#     def swaptwonumber(self):
#         a = int(input("Enter the value of a: "))
#         b = int(input("Enter the value of b: "))

#         print(f"Before swaping the valuse. value of a is: {a} and value of b is: {b}")

#         a = a + b
#         b = a - b
#         a = a - b
#         print(f"After swaping the valuse. value of a is: {a} and value of b is: {b}")


# swap = SwapTwo_Numbers()
# swap.swaptwonumber()

class NumberSwapper:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def swapper(self):
        self.num1 = self.num1 + self.num2
        self.num2 = self.num1 - self.num2
        self.num1 = self.num1 - self.num2

num1 = int(input("Enter the value of num1: "))            
num2 = int(input("Enter the value of num2: "))
swap = NumberSwapper(num1, num2)   
print(f"Before swaping the valuse. value of num1 is: {swap.num1} and value of num2 is: {swap.num2}") 
swap.swapper()   
print(f"After swaping the valuse. value of num1 is: {swap.num1} and value of num2 is: {swap.num2}")     
