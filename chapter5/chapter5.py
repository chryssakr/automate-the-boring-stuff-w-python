# Dictionaries
# They are mutable. They contain key: value pairs in {}

my_cat = {
    "size": "fat",
    "colour": "gray",
    "disposition": "loud"
}
print(my_cat["colour"])

# Lists vs Dictionaries
# lists: ordered, dict: unordered. Two dicts with different order but same values are equal.

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) # True

# KeyError: the key I'm trying to access does not exist
# With dict you can organise data in powerful ways
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# keys(), values() and items()