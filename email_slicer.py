# Email slicer project

# declare a variable to store user input
# remove inadvertent leading and trailing whitespace using the strip() function
email = input("What is your email address?: ").strip()

# Slice out user name and store in variable
user = email[: email.index("@")]

# Slice out domain name and store in variable
domain = email[email.index("@") + 1 :]

# Format message
# output = "Your username is {} and your domain name is {}".format(user, domain)

# NOTE: Since the introduction of f-strings in Python 3.6, the correct way to
# do this would be:
output = f"Your username is [{user}] and your domain name is [{domain}]"

# Display output message
print(output)
