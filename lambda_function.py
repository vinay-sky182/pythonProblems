# A function which has no name, and can intake any number of arguments and one expression is lambda function

# sum = lambda a, b : a + b

# print(sum(5, 4))



# Using *args in python: When we use *args as a function parameter then while caling the function we can pass any number of single value arguments to the parameter of function

""" def sample(*args): # Using *args as a function parameter
    for i in args:
        print(i)

sample(9,1)   

def sample(a, b, c, d):
    print(a, b, c, d)

args = [9, 1, 5, 7]   
sample(*args) """ # Using *args as argument in function calling


# Using **kwargs in python: When we use **kwargs as a function parameter then while caling the function we can pass any number of key value arguments

def sample(**kwargs):
    for k, v in kwargs.items():
        print(k, v);

sample(name = "Vinay", location = "Gurgaon")

def sample(name, location):
    print(name, location)

d = {"name" : "Rudra", "location" : "Unnao"} 
sample(**d)


