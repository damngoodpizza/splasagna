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

# When dealing with a list, two ways we can remove an element are:

cities = ["Atlanta", "New York", "Philadelphia", "Los Angeles", "Detroit", "Tampa"]

# The remove method, variable.remove("Atlanta")
# NOTE: You must be able to address the specific element. If the exact element is
# unknown, this won't work.
print(cities)
cities.remove("Atlanta")
print(cities)


# Sometimes, you need to remove a certain index, or slice of indexes, from a list.
# We can delete index zero like so:
example = [1, 2, 3, 4, 5]
del example[0]
print(example)

# Unlike the remove method, the del method can target a specific index:
example = ["a", "b", "c", "a", "b"]
print("This is our example: " + str(example))
example.remove("a")
print("The remove method only removes the first instance: " + str(example))
example = ["a", "b", "c", "a", "b"]
print("Let's revert our list: " + str(example))
del example[3]
print("And use del to target the second instance of 'a': " + str(example))

# How would we go about deleting a slice?
example = ["a", "b", "c", "a", "b"]
del example[1:4]
print("In this example, we slice 'b, c, and a' from the middle of the list" + str(example))

# More ways to add items to lists:
# Only lists can be added to lists using the addition operator.
a = [5, 12, 72, 55, 89]
a = a + [1]
print(a)

# What if we want to add a string to our list?
a = a + ["test"]
print(a)

# We can also use the list method, but the behavior is different:
a = a + list("test")
print(a)
# NOTE: This method doesn't work for integers, since they aren't an iterable data type, and
# therefore cannot be converted into lists.

# We could still add numbers as a string like so:
a = a + list(str(123))
print(a)
# NOTE: Pay attention to the quotes around these numbers. These are strings, not integers.

# What if I wanted to add some integers as a single element?
# reset 'a'
a = [5, 12, 72, 55, 89, 1]
a = a + [[5,6,7,8]]
print(a)

# You could also use the append method:
a.append([10,11,12,13])
print(a)

# What if we want to insert 100 into our list between 12 and 72?
# reset 'a'
a = [5, 12, 72, 55, 89, 1]
a.insert(2,100)
print(a)

# How about inserting a slice?
a.insert(2,[10,20,30])
print(a)

# !!!!! SUPER IMPORTANT !!!!!
# Lists are mutable, and can therefore be overwritten. For example, why does the following work?
a = "text string"
a = a + " new"
print(a)
# And the following doesn't?
a = [1,2,3]
a = a.append(4)
print(a)
a = type(a)
print(a)
# This is because a.append(4) returns a value of 'None', overwriting the value of 'a' with 'None'



# What Are Tuples
# -------------------------------------------------------------------

# Tuples are an immutable data type
# Tuples are an iterable data type

our_tuple = 1,2,3,"a","b","c"
result = type(our_tuple)
print(result)
print(our_tuple)

# While the above works, it is more common to surround our tuple with parenthesis for readability.
our_tuple = (1,2,3,"a","b","c")
print(result)
print(our_tuple)

# Being an iterable data type, we can look at specific elements or slices:
result = our_tuple[0:3]
print(result)

# The only real difference between tuples and lists is that you cannot change a tuple after creation.
# Tuples, like strings, are immutable.
our_list = [1,2,3,4,5,6,7]
our_list[2] = 100
print(our_list)
# We can change the 2nd element in our_list to 100.
# our_tuple = (1,2,3,4,5,6,7)
# our_tuple[2] = 100
# print(our_tuple)
# When we try to do the same with our_tuple, we get an error as the tuple object doesn't support
# item assignment because it is immutable.

# You can use the tuple() function to convert other data types to a tuple.
a = [1,2,3]
print(a)
a = tuple(a)
print(a)
result = type(a)
print(result)

# You can do multiple assignment with tuples:
(a,b,c) = 1,2,3
print(a)
print(b)
print(c)

# You can also do multiple assignment with lists:
d,e,f = [4,5,6]
print(d)
print(e)
print(f)

# You can also do multiple assignment with strings:
g,h,i = "789"
print(g)
print(h)
print(i)


