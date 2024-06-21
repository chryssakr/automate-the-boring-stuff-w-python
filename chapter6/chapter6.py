# # Manipulating strings
# # String Literals
# # 'this is a string' "that's a string as well"

# # Escape characters
# # \' \" \t (tab) \n (new line) \\ (backslash)
# print('With escape characters I can use " inside the string.')
# print("Hello there!\nHow are you?\nI'm doing fine.")

# # Raw strings
# # If I place an r before the quotation mark of a string, it makes it raw
# # a raw string completely ignores all escape characters and prints any backslash in the string
# # useful for strings with many backslashes, such as windows file paths
# print(r"That is Carol\'s cat.")

# # Multiline strings with triple quotes
# # Any quotes, tabs, or newlines in between the “triple quotes” are considered part of the string
# # Python’s indentation rules for blocks do not apply to lines inside a multiline string.
# # Escaping single and double quotes is optional in multiline strings.

# print(
#     """Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# Sincerely,
# Bob"""
# )

# # Multiline comments with triple quotes
# """This is a test Python program.
# Written by Al Sweigart al@inventwithpython.com
# This program was designed for Python 3, not Python 2.
# """

# # Indexing and Slicing Strings
# # Strings work the same way as lists when it comes to indexing and slicing
# # Slicing does not modify the original string
# spam = "Hello, world!"
# print(spam[0])
# print(spam[4])
# print(spam[-1])
# print(spam[0:5])  # [0,5), the ending is not included
# print(spam[:5])
# print(spam[7:])
# fizz = spam[0:5]
# print(fizz)

# The in and not in operators with strings
print("Hello" in "Hello World!")  # True
print("HELLO" in "Hello, World")  # False
print("" in "spam")  # True
print("cats" not in "cats and dogs")  # False
print(True, True, True != True, True, True)
