# Section 6: If This, Then That: Logic and Conditional Flow in Python
# ===================================================================

# Booleans & Comparison Operators
# -------------------------------------------------------------------

# Booleans are the building blocks of logic systems.
# Booleans only have two values, True and False.

# Comparison Operators
# >  - greater than operator
# >= - greater than or equal to operator
# <  - less than operator
# <= - less than or equal to operator
# == - equality operator 'Not to be confused with the assignment operator (=)'
# != - not-equal to operator


# Let's determine if 2 is greater than 3:
x = 2 > 3
print(x)
# This returns 'False', as 2 is not greater than 3.

# Let's determine if 2 is less than 3:
x = 2 < 3
print(x)
# This returns 'True', as 2 is less than 3.

# Let's determine if 2 is equal to 3:
x = 2 == 3
print(x)
# This returns 'False', as 2 is not equal to 3.

# Let's determine if 2 is equal to 2:
x = 2 == 2
print(x)
# This returns 'True', as 2 is equal to 2.

# Let's determine if 2 is not equal to 3:
x = 2 != 3
print(x)
# This returns 'True', as 2 is not equal to 3.

# Let's determine if 2 is not equal to 2:
x = 2 != 2
print(x)
# This returns 'False', as 2 is not not equal to 2.



# Python if Statement
# -------------------------------------------------------------------

# An if statement allows us to execute a certain piece of code only
# if a certain condition is True.

# if condition:

if True:
    print("It worked!")


num1 = 100
num2 = 100
if num1 > num2:
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

# In the preceding code example, what happens if num1 and num2 are equal?
# Our comparison operator, >, compares the two variables and returns a
# boolean of 'False', as 100 is not greater than 100. Therefore, the code
# under the else statement is executed.
# We can use the elif statement to resolve this:

if num1 > num2:
    print("num1 is greater than num2")
elif num2 > num1:
    print("num2 is greater than num1")
else:
    print("The numbers are equal.")

# We can use elif to check for multiple conditions:
# if condition:
#    code1
# elif condition2:
#    code2
# elif condition3:
#    code3
# else:
#    code4


# Python Logical Operators - Part 1 (not + and)
# -------------------------------------------------------------------

# not - Reverse the result, returns 'False' if the result is true

x = not True
print(x)

x = not False
print(x)

x = not 3 > 1
print(x)

x = not 1 > 3
print(x)

x = 10
y = 20
if not y < x:
    print("if - It worked")


# and - Returns 'True' if both statements are true

c = 10
d = 5
if c > 10 and d > 1:
    print("and - It worked")

# The preceding code example returns 'False' as c is not greater than 10
# Both statements must be true to return 'True'
# For example:

c = 15
d = 5
if c > 10 and d > 1:
    print("and - It worked this time")

# How can we combine not and and?
c = 10
d = 5
if not (c > 10 and d > 1):
    print("and - It worked again")



# Python Logical Operators - Part 2 (or)
# -------------------------------------------------------------------

# or - Returns 'True' if either statement is true

c = 5
d = -1
if c > 1 or d > 1:
    print("or - It worked")

# How can we combine not and or (nor)?
c = 10
d = 5
if not (c > 11 or d > 6):
    print("or - It worked again")

# How can we combine and + or?
c = 6
d = 2
if (c > 5 and d > 5) or (c > 1 and d > 1):
    print("Combining and + or - It worked")

# We can also utilize not in the preceding example:
c = 6
d = 2
if not ((c > 5 and d > 5) or (c > 1 and d > 1)):
    print("Combining not + and + or - It worked")



# Section 7: Hold This For Me: Python Datastructures
# ===================================================================

# What Are Lists
# -------------------------------------------------------------------

# We use brackets[] to create a list.
# Python lists can include multiple data types.
# Python lists are iterable.

our_list = [1, 2, 3, 4, 5]
print(our_list)
output = type(our_list)
print(output)

# How can we access a particular element?
cities = ["Atlanta", "New York", "Philadelphia", "Los Angeles", "Detroit", "Tampa"]
print(cities[3])
# Better yet, declare a variable
cities = ["Atlanta", "New York", "Philadelphia", "Los Angeles", "Detroit", "Tampa"]
output = cities[2]
print(output)

# Remember that we can count from right to left:
cities = ["Atlanta", "New York", "Philadelphia", "Los Angeles", "Detroit", "Tampa"]
output = cities[-2]
print(output)

# If you want to take out more than one element, you will need to slice.
cities = ["Atlanta", "New York", "Philadelphia", "Los Angeles", "Detroit", "Tampa"]
output = cities[:3]
print(output)

# Python lists can contain other lists.
another_list = [1, 2, 3, [30, 40, 50], 4, 5, 6]
print(another_list[3])
# NOTE: The entire nested list is in position 3.
# What if we wanted to access a single element in our nested list?
print(another_list[3][1])
# The first number denotes the element in position 3 (the entire list)
# The second number denotes the element in position 1 within the nested list.

# You can slice within these as well:
print(another_list[3][1:])



our_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(our_table[0])
print(our_table[1][1:])
