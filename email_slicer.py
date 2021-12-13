# Email slicer project

# declare a variable to store user input
# remove leading 
# The user may accidentally input spaces before or after their email address.
# We can utilize the strip string method 'strip()' to remove unwanted spaces.

email = input("What is your email address?: ").strip()

# Slice out user name
user = email[: email.index("@")]

# Slice out domain name
domain = email[email.index("@") + 1 :]

# Format message
output = "Your username is {} and your domain name is {}".format(user, domain)

# Display output message
print(output)
