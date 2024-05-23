""""
print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)
"""

"""""
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
"""
""""
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
"""

"""
import random
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']
print(messages[random.randint(0, len(messages) - 1)])
"""
"""
name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('* * * ' + i + ' * * *')
"""

# name = "Zophie a cat"
# new_name = name[:7] + "the" + name[8:]
# print(new_name)

# eggs = [1, 2, 3]
# eggs = [4, 5, 6] # it does not modify(we don't have a new list value), it overwrites an entirely new and different list value
# del eggs[2]
# eggs.append(7) # that mutates

# def eggs(some_parameter):
#     some_parameter.append('Hello')

# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

# tuples
# They use () instead of [] in lists. They are immutable.

# eggs = ("hello", 42, 0.5)
# eggs[1] = 99 # that would flag a TypeError

# print(type(("hello",))) # when I have a single value, a trailing comma indicates it as a tuple
# print(type(("hello"))) # this is considered to be a string

# I can convert types with list() and tuple()

# print(tuple(['cat', 'dog', 5]))
# print(list(('cat', 'dog', 5))) # in this way I have a mutable version of a tuple
# print(list('hello')) # returns ['h', 'e', 'l', 'l', 'o']

# References
# print(id('Howdy')) # the numeric memory address where the string is stored
# bacon = 'Hello'
# print(id(bacon))
# bacon += ' world!' # strings are immutable, so this creates a new string
# print(id(bacon)) # it will have a new memory address

# eggs = ['cat', 'dog']
# print(id(eggs))
# eggs.append('moose') # lists are mutable, so this still refers to the same list
# print(id(eggs)) # it will be the same as before

# # copy module, copy() and deepcopy()
# # copy.deepcopy: to copy lists that contain lists
# import copy
# spam = ["A", "B", "C", "D"]
# print(id(spam))
# cheese = copy.copy(spam) # cheese will be a different list with a different id
# print(id(cheese))
# cheese[1] = 42 # it does not affect spam
# print(spam)
# print(cheese)

