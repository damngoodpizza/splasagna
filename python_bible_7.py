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
output = cities.remove("Atlanta")
print(output)


# Sometimes, you need to remove a certain index, or slice of indexes, from a list.
# We can delete index zero like so:
list = [1, 2, 3, 4, 5]
del list[0]
print(list)

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

