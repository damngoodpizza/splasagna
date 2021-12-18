# Strings are an iterable data type which means you can go step-by-step along it until you get to the end.
# Each of these steps is called an element. Each element has a number which refers to its position.
# This number is called an index. By using the index you get to the element.

# Slicing code example that returns the element located in position 4:

string = "abcdef123456"
output = string[4]
print(output)

# What if we want to get more than a single letter?
# variable[start:end:step]
output = string[0:6:1]
print(output)

# A shortcut we can use if we want a slice to go all the way to the end of the string:
# A step length of 1 is assumed.
output = string[4:]
print(output)

# What if we want from position 4 to the end of the string in steps of 2?
output = string[4::2]
print(output)

# What if we want everything up to a certain position?
# A step length of 1 is assumed.
output = string[:7]
print(output)

# To reverse a string, or portion of a string:
output = string[::-1]
print(output)