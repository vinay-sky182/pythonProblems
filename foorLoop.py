# print the elements of the following list using for loop

""" num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in num:
    print(el) """

# search for a number x in this tuple using for loop 

""" idx = 0
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100) 
x = 25
for el in tup:
    if(el == x):
        print("found at index", idx)
    idx += 1  """   

# print the numbers from 1 to 100

""" for el in range(1, 101):
    print(el) """

# print the numbers from 100 to 1   

""" for el in range(100, 0, -1):
    print(el) """

# WAP to print multiplication tble of a number n

""" num = int(input("Enter the number: "))
for i in range(1, 11):
    print(num * i) """


# pass statement : -  pass is a null statement that does nothing. it is used as a placeholder for future code.   

""" for el in range(1, 10):
    pass

print("I'll come back after some time") """


# WAP to find the sum of first n numbers using while/ for loop

""" sum = 0
n = 10
i = 1
while(i <= n):
    sum = sum + i
    i += 1
print(sum) """

""" n = 10
sum = 0
for i in range(1, n+1):
    sum += i
print(sum) """    

# WAP to find the factorial of first n numbers using for/while loop

""" n = 3
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact) """

fact = 1
n = 4
i = 1
while(i <= n):
    fact = fact * i
    i += 1
print(fact)