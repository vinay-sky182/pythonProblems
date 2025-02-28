""" num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(f"Entered number {num} is Even")
else :
    print(f"Entered number {num} is Odd")     """

####################################################################

""" a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a>b and a>c):
    print(f"a {a} is greatest amoung three numbers")
elif(b>a and b>c):
    print(f"b {b} is greatest amoung three numbers") 
else:
    print(f"c {c} is greatest amoung three numbers")   """  

####################################################################

""" list1 =[1,2,1]  
print("list1: ", list1) 
copy_list1 = list.copy(list1)
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not Palindrome") """

####################################################################

tup = ("C", "D", "A", "A", "B", "B", "A")
print (tup.count("A"))

my_list = list(tup)
my_list.sort()
print(my_list)