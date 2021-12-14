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
