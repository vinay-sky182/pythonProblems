# Swap two numbers without using third variable.

class SwapTwo_Numbers:

    def swaptwonumber(self):
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))

        print(f"Before swaping the valuse. value of a is: {a} and value of b is: {b}")

        a = a + b
        b = a - b
        a = a - b
        print(f"After swaping the valuse. value of a is: {a} and value of b is: {b}")


swap = SwapTwo_Numbers()
swap.swaptwonumber()

