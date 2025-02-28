class A:

    a = 9

    def method_a(self):
        print("Inside method_A")


class B(A):

    b = 10

    def method_b(self):
        print("Inside method_b")   


obj = B()         
print(obj.a)
print(obj.b)
obj.method_a()
obj.method_b()