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

# # The in and not in operators with strings
# print("Hello" in "Hello World!")  # True
# print("HELLO" in "Hello, World")  # False
# print("" in "spam")  # True
# print("cats" not in "cats and dogs")  # False
# print(True, True, True != True, True, True)

# # Putting strings inside other strings
# # We have: string concatenation: "string" + str(age)
# # string interpolation: "string %s" %(age)
# # and f-strings: f"string {age}"
# name = "Joe"
# age = 2
# print("My name is %s. I am %s years old." % (name, age))
# print(f"Next year I will be {age + 1}.")

# # The upper(), lower(), isupper(), and islower() Methods
# # the upper() and lower() methods return uppercase and lowercase
# # They don't change the string, they return new values
# spam = "Hello, world!"
# print(spam.upper())
# print(spam.lower())

# # isupper() and islower() check the case of a string and return bool
# spam = "Hello, world!"
# print(spam.islower())
# print(spam.isupper())

# # I can chain those methods
# print("Hello".upper().lower().upper())
# print("HELLO".lower().islower())

# # isX methods
# # They return bool, useful for data validation
# # isalpha(): if it consists only of letters and isn't blank
# # isalnum(): if it consists only of letters, and numbers and isn't blank
# # isdecimal(): if it consists only of numeric characters and isn't blank
# # isspace(): if it consists only of spaces, tabs, and newlines and isn't blank
# # istitle(): if it consists only of capitalised words and isn't blank

# while True:
#     age = input("Enter your age:")
#     if age.isdecimal():
#         break
#     print("Non-valide format. Please enter a number for your age.")
# while True:
#     password = input("Select a new password (letters and numbers only):")
#     if password.isalnum():
#         break
#     print("Non-valide format. Passwords can only have letters and numbers.")

# The startswith() and endswith() Methods

# print(", ".join(["cats", "rats", "bats"]))
# print(" ".join(["My", "name", "is", "Simon"]))
# print("My name is Simon".split())
# print("My name is Simon".split("i"))

# spam = """Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."

# Please do not drink it.
# Sincerely,
# Bob"""

# print(spam.split("\n"))

"""
isX Methods
startswith(), endswith() Methods
join() and split() Methods
partition() Method
    returns a tuple of three substrings for the “before,” “separator,” and “after”
rjust(), ljust(), and center() Methods
    justify text
strip(), rstrip(), and lstrip() Methods
    remove white space
ord() function to get the code point of a one-character string
chry() function to get the one-character string from a code point
"""

# before, sep, after = "Hello, world!".partition(" ")
# print(before, sep, after)
# print("Hello".rjust(10))  # right justify Hello in a string of total length: 10
# print("Hello".rjust(20, "*"))
# print("Hello".center(20, "="))

# spam = "    Hello, World    "
# print(spam.rstrip())

# spam = "SpamSpamBaconSpamEggsSpamSpam"
# print(spam.strip("ampS"))  # the order of the letters doesn't matter
# print(ord("A"))
# print(chr(65))

"""
Copying and Pasting Strings with the pyperclip Module
sys.argv is a list where:
    sys.argv[0] → The script name (e.g., "mclip.py")
    sys.argv[1] → The first argument provided by the user
    sys.argv[2], sys.argv[3], etc. → Additional arguments (if any)
"""
import pyperclip

# pyperclip.copy("Hello, world!")
# print(pyperclip.paste())
text = pyperclip.paste()
lines = text.split("\n")
for i in range(len(lines)):
    lines[i] = "*" + lines[i]
text = "\n".join(lines)
print(text)
pyperclip.copy(text)
print("Your newly formatted text has been copied to the clipboard")
