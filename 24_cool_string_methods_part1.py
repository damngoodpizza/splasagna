
# ================================ #
# 24. Cool String Methods - Part 1 #
# ================================ #

# count string method

text = "I like to fly airplanes on the weekend."
char = "e"
total = text.count(char)
string = "The total instances of [{}] in this text: {}"
output = string.format(char, total)
print(text)
print(output)

originaltext = "Text I Want To Change Case Of"
print("Original Text: " + originaltext)
print("Lower Case: " + originaltext.lower())
print("Upper Case: " + originaltext.upper())
print("Capitalized: " + originaltext.capitalize())
print("Title: " + originaltext.title())
# strings are an immutable (cannot be changed) data type


