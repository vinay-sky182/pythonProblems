# WAP to add two numbers

""" num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print(f"Sum of two number is : {sum}") """

# WAP to find Maximum of two numbers

""" def maximum(x, y):

    if (x >= y):
        return print(f"{x} is the maximum number")
    else :
      return print(f"{y} is the maximum number")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))    
maximum(a , b)  """


# WAP for factorial of a number

""" n = int(input("Enter a number: "))

if (n==1 or n==0):
    print(f"Factorial is: ", 1)
else:    
  fact = 1
  for i in range(1 , n+1):
    fact *= i
  print(f"factorial is : {fact}") """


# WAP for Simple intrest 

""" def simpleIntresr(p, t, r):
   print("The principal amount is", p)
   print("The time period is", t)
   print("The rate of intrest is", r)

   si = (p * r * t)/100

   print(f"The Simple Intrest is : {si}")

P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
simpleIntresr(P, T, R) """   


# WAP to check number is Armstrong Number or not

""" num1 = input("Enter a number: ")
l = len(str(num1))
num = int(num1)

sum = 0
for d in num1:
   sum += int(d)**l
if (sum == num):
   print(f"{num} is an Armstrong Number")
else :
   print(f"{num} is not an Armstrong Number")  """ 


# WAP to find area of a circle
   
""" radius = int(input("Enter the value of radius: "))
pi = 3.1415

Area_of_circle = pi * (radius) ** 2

print(f"Area of circle : {Area_of_circle}") """


# WAP print all Prime numbers in an Interval of 1 to 100

for i in range(1, 11):
   
   if i > 1:
       for j in range(2, i):
           if (i % j == 0):
               break
       else:
           print(i)
      
        


  
            
            
  