word = "supercalifragilisticexpialidocious"
print("Our word is: " + word)

# Suppose we want to store the 'd' in our string to a variable.
# We could count up from the beginning of the string like this:
var = word[27]
print("Counting from left to right, the element in position 27 is: " + var)
# This function counts from the left to the right. The first
# position is 0, so our 'd' is in the 27th position, even though
# it is actually the 28th letter in our word.

# We are also able to count in the other direction like so:
var = word[-7]
print("Counting from right to left, the element in the -7th position is: " + var)
# In this example, the function counts from right to left. The
# first position is -1, so out 'd' is in the -7th position.

# We can use the index function to determine the position of
# elements in our word.
var = word.index("cali")
print("The element 'cali' starts at position: " + str(var))
# In this example, the element 'cali' starts in the 5th position.

# Where does the element 'fragi' start?
var = word.index("fragi")
print("The element 'fragi' starts at position: " + str(var))

# We can utilize the index function to return a specific portion of a string like so:
var = word[word.index("cali"):word.index("fragi")]
print("We used the index function to store the element [" + var + "] to a variable.")

# Suppose we want to store an element that runs to the end of the string?
var = word[word.index("docious"):]
print("We used the index function to store the element [" + var + "] to a variable.")

# NOTE: The index function only returns the first instance of the element.
# For example, suppose that we want to store the element 'fragilistic':
var = word[word.index("frag"):word.index("exp")]
print("We used the index function to store the element [" + var + "] to a variable.")
# The preceding example works. However, take the following example:
var = word[word.index("frag"):word.index("e")]
print("We used the index function to store the element [" + var + "] to a variable.")
# The preceding example doesn't return the expected element. This is because
# as we iterate along the string, we encounter an 'e' before the 'e' following
# 'fragilistic'. We resolve this by ensuring our index is unique in the string.

# NOTE: Strings are an iterable and immutable data type.


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


