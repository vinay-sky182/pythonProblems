# WAP to print numbers from 1 to 100

""" i=1
while i<=100:
    print(i)
    i+=1 """

# WAP to print numbers from 100 to 1

""" i=100
while i>=1:
    print(i)
    i-=1 """

# WAP to print multiplication tble of a number n

""" n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n*i)
    i+=1 """

 # WAP to print the element of the following list usin a loop   

""" nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lenght = len(nums)
i=0
while i<=lenght-1:
    print(nums[i])
    i+=1 """

# Search for a number x in this tuple using loop

""" nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 9
i = 0
while i< len(nums):
    # print(nums[i])
    if (nums[i]==x):
        print("Found at index", i)
        break
    i+=1 """

# break keyword

""" i = 1
while i <= 10:
    print(i)
    if(i == 8):
        break
    i += 1

print("End of loop") """   

# continue keyword

""" i = 1
while i <= 10:
    if(i == 5):
        i += 1
        continue # continue ke baad ke steps skip ho jayege
    print(i)
    i +=1 """

# WAP to print even numbers from 1 to 10
    
i = 1
while i <= 10:
    if(i % 2 != 0):
        i += 1
        continue
    print(i, end=' ')
    i +=1

# end=' ' it is used to print without a newline 