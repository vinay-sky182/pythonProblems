""" 
Collection is nothing but data types in python which allow us to store multiple value in single variable are known as Collection data types.

There are 4 collection data types in python:

1.) list []
2.) tuple ()
3.) set {}
4.) dictionary {"key" : "value"} """


""" 1) List [] The elements within a list can be mutable(changeable) or immutable(unchangeable). Lists themselves are mutable """

colors = ["orange", "green", "white", "blue"];

print(colors[0]);
print(colors[1]);
print(colors[2]);
print(colors[3]);

print("************************");



""" functions of list """


# 1.) len()

print("length of a list:", len(colors));

print("************************");
# 2.) for loop with range with list

for i in range(len(colors)):
    print(colors[i]);

print("************************")

# 3.) for-each loop with list

for name in colors:
    print(name);

print("************************");

# 4.) Updating the elements in the list

print("original list:", colors);

print("************************");

colors[2] = "grey";

print("updated list:", colors);

print("************************");

# 5.) Appending the elements to the end of the list

print("before appending list:", colors);

print("************************");

colors.append("olive");

print("after appending list:", colors);

print("************************");


# 5.) Inserting the elements at a perticular index

print("before inserting an element in list:", colors);

print("************************");

colors.insert(2, "yellow");

print("after inserting an element in list:", colors);

print("************************");

# 6.) Removing the elements at a perticular index

print("before removing an element from list:", colors);

print("************************");

colors.remove("yellow")

print("after removing an element from list:", colors);

print("************************");

# 7.) Removing the last element from the list

print("before poping last element from list:", colors);

print("************************");

colors.pop();

print("after poping last element from list:", colors);

print("************************");

# 8.) Removing the elements using their index using pop(index) and returns the removed element

print("before removing element by using pop(index) from list:", colors);

print("************************");

colors.pop(3);

print("after removing element by using pop(index) from list:", colors);

print("************************");

# 9.) Removing all the elements from the list using clear()

""" 
print("before removing all elements by using clear() without deleting the list:", colors);

print("************************");

colors.clear();

print("after removing all elements by using clear() without deleting the list:", colors);

print("************************"); """


# 10.) Reversing the elements of the list using reverse()

print("before Reversing the elements of a list by using reverse():", colors);

print("************************");

colors.reverse();

print("after Reversing the elements of a list by using reverse():", colors);

print("************************");

# 11.) Sorting the elements of the list in alphabetical order using sort()

print("before Sorting the elements of a list by using sort():", colors);

print("************************");

colors.sort();

print("after Sorting the elements of a list by using sort():", colors);

print("************************");

# 12.) Nested list in python

a = [9,[6, 0, 6, 8], 5, 7]

print(a[1]);

print("************************");

print(a[1][3]);

print("************************");

# 13.) Forward and Backward index

num = [9, 1, 5, 7]

print(num[-2]) # backward index

print("************************");

# 14.) Slicing lists

#   a) num[1:3] - index 1 to 3rd element
#   b) num[:] - index 0 to last element (till length)
#   c) num[:4] - index 0 to 4th element

print("before Slicing the list:", num);

print("************************");

print(num[1:3]); # index (included) : position (excluded) (given_num - 1 = index)

print("after Slicing the list:", num);

print("************************");


# 15.) Finding the number of times the element is repeated in the list using count()

digits = [9, 1, 5, 7, 6, 0, 6, 8, 9, 9, 5, 9, 9]

print("Occurenc of element 9 is:", digits.count(9))

print("************************");

# 16.) Finding the maximum and minimum elements in the list using max and min()

print("Maximum value from given list is:", max(digits))
print("Minimum value from given list is:", min(digits))

print("************************");

# 17.) Finding the sum of elements in the list using sum()

print("Sum of the elements of given list:", sum(digits))

print("************************");

# 18.) Finding the data type of the list using type()

print("Data type is:", type(digits))

print("************************");

# 19.) Deleting the list using delete list_name

print("before Deleting the list:", digits);

print("************************");

""" del digits

print("after Deleting the list by using del:", digits);

print("************************"); """

# 20.) Using in and not in operator with list to check whether an element is present in the list or not, returns true or false

print("Is element 5 present within the list:", 5 in num)

print("************************");

print("Is element 0 present within the list:", 0 in num)

# 21.) Concatenating two lists using + operator

""" print("after Concatenating num and digits two lists:", digits + num) """

print("************************");

# 22.) Extending the list

num.extend(digits)

print("after Extending the num list:", num)

print("************************");


# ************************************************************************************************************************************* #

""" 2) Tuple () "The elements within a tuple can also be mutable(changeable) or immutable. However, tuples themselves are immutable(unchangeable)" """

# diffrence b/w list and tuple

""" 
1.) List elements can be updated hence it is called mutable(changeable) but Tuple elements can not be updated hence it is called immutable(unchangeable).  
2.) In tuple we can not use append(), insert(), remove(), pop(), sort() and reverse() comands because tuple is immutable(unchangeable).
3.) If we create a list inside of a tuple only, list will be mutable 
"""

#  functions of Tuple () 

a = (9, 1, 5, 7)

print("Tuple is:", a)

print("************************");

print(type(a))

print("************************");

print("accessing the element using index:", a[2])

print("************************");

print("Length of tuple:", len(a))

print("************************");

# Typecast String into tuple

b = tuple("vinay")

print(b)

print("************************");


# """ Set - Collections  {} """

""" List [] vs Tuple () vs Set {} """


""" 
1.) List is changeable, Tuple is not changeable but Set is also changable. However, the elements within a set must be immutable(unchangeable). 
2.) List has indexing, Tuple also has indexing but Set dosen't support indexing hence duplicates are ignored it will have unique values.
3.) List and Tuple's elements are stored in the same given order but in Set elements are stored in random order.
"""

#  functions of Set {} 

a = {9, 1, 5, 7}

print("Print the set:", a)

print("************************");

print("Data_Type of a:", type(a))

print("************************");

# length of set using len()

print("Find the length of a:", len(a))

print("************************");

# adding an element within set using add()

print("before Adding the value in set by using add():", a);

print("************************");

a.add(8)

print("after Adding the value in set by using add():", a);

print("************************");

# adding multiple elements within set using update()

print("before Adding the multiple values in set by using update():", a);

print("************************");

a.update([4,12])

print("after Adding the multiple values in set by using update():", a);

print("************************");

# removing an element from set using remove()

print("before Removing the element from set by using remove():", a);

print("************************");

a.remove(5)

print("after Removing the element from set by using remove():", a);

print("************************");

# discard an element from set by using discard(), if we pass an element which is not available within set discard 'function' will not give any error it will ignore but if we pass the same element with remove function it will give "KeyError" error hence we can say that discard is a smart element removing function.

""" a.remove(15) """

a.discard(15)

# randomly rmoving the value from set using pop()

print("before randomly Removing the vlaue from set by using pop():", a);

print("************************");

a.pop()

print("after randomly Removing the element from set by using pop():", a);

print("************************");

# rmoving all the values from set using clear()

print("before Removing all the elements from set by using clear():", a);

print("************************");

""" a.clear()

print("after Removing all the elements from set by using clear():", a);

print("************************"); """

# ******************************************************************************************* #

""" 

empty_tuple = ()
# or
empty_tuple = tuple()

empty_set = set()

empty_dict = {}
# or
empty_dict = dict()
# or
empty_dict = {key: value for key, value in []}

"""

# deleting a set

print("before Deleting the set by using del 'keyword':", a);

print("************************");

""" del a

print("after Deleting the set by using del keyword:", a);

print("************************");  """

# for loop [for i in range()] with range() - is not possible with set 

# we can use for each loop with set

for e in a:
    print(e)

""" 'Set' can only nest Tuple it can not nest List and Set. 
Sets can only contain immutable (unchangeable) elements. This is because sets rely on the immutability of their elements to maintain their uniqueness """

a= {9, (6, 0 ,6 ,8), 5, 1, 7}

# Converting a List to a Set

a = [9, 1, 5, 7] # list
b = set(a) # conversion from list to set
print("type of b:", type(b))

print("************************");  

# Union

a = {9, 1, 5, 7}
b = {8, 5, 6, 1}

print("Union of two sets a and b:", a.union(b)); # Union will return a set of 6 elements because element 1 and 5 are twice it will concider them only once. either we can use union() or we can use or '|' operator.

print("************************"); 

print("Union of two sets a and b:", a | b);

print("************************"); 

# Intersaction

print("Intersaction of two sets a and b:", a.intersection(b)); # it will only give the commman values from both sets

# either we can use intersection() or we can use '&' operator

print("************************"); 

print("Intersaction of two sets a and b:", a & b);

print("************************");  

# Difference 

print("Difference of two sets a and b:", a.difference(b));
print("************************"); 

print("Difference of two sets a and b:", a - b);
print("************************");  # {9, 7}

# Symmetric difference

print("Symmetric_Difference of two sets a and b:", a.symmetric_difference(b));
print("************************"); 

print("Symmetric_Difference of two sets a and b:", a ^ b); # {6, 7, 8, 9}
print("************************"); 


# ******************************************************************************************* #

""" Dictionary - Collection """

