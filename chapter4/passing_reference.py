def eggs(some_parameter):
    some_parameter.append("Hello")  # lists are mutable so this gets modified in place


spam = [1, 2, 3]
eggs(spam)  # spam gets copied to some_parameter and they both refer to the same list
print(spam)
