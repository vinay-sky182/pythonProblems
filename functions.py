# WAF to print the length of a list. (list is the parameter)

cars = ["Audi", "BMW", "Maserati", "Aston Martin", "Porsche", "Karman Ghia"]

""" def print_len(list):
    print(len(list))

print_len(cars) """

# WAF to print the elements of a list in a single line. (list is the parameter)

heroes = ["Iron Man", "Wolvarine", "Deadpool", "Spider Man", "Shaktiman", "Krish", "Flash"]

""" def print_list(list):
    for i in list:
        print(i, end=' ')

print_list(heroes) """


# WAF to find the factorial of n. (n is the parameter) 

""" def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)    

cal_fact(4) """

# WAF to convert USD to INR

""" def convertor_USD_INR(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

convertor_USD_INR(3)  """   


""" def check_Num():
    num = int(input("Enter a number: "))
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

check_Num() """  


# Recursion :- A recursive fun() is one which calls itself. During each recursive call a given problem is broken into smaller problem.
# Importent point is to ensure that recursion terminates.
# Base Case : It is a case where the recursion terminates.
# Recursive Case : It is a case where fuv() calls itself to performe subtask.

""" def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)  """  


# Write a Recursive function to calculate factorial


""" def recursion_fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * recursion_fact(n - 1)
    
print(recursion_fact(5)) """   


# Write a Recursive function to calculate the sum of the first n natural numbers.


def recursive_sum(n):
    n = 10
    if(n == 0):
        return 0
    else:
        recursive_sum(n - 1) + n


# Write a Recursive function to print all elements in a list
        

def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

# cars = ["Audi", "BMW", "Maserati", "Aston Martin", "Porsche", "Karman Ghia"]

print_list(cars)    
       

       

    