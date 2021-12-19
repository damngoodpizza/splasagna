known_users=["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

# When dealing with lists, the len() function lets us know how many elements are in our iterable.
# print(len(known_users))

while True:
    print("Hi! My name is Travis.")
    # You can use multiple methods together
    name = input("What is your name?: ").strip().capitalize()
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").strip().lower()
        if remove == "y":
            known_users.remove(name)
        elif remove =="n":
            print("No problem. I didn't want you to leave anyway!")
    else:
        print("I don't think we've met {}".format(name))
        add_me = input("Would you like to be added to the system? (y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries. See you around!")

