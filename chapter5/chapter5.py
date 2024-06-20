# # Dictionaries
# # They are mutable. They contain key: value pairs in {}

# my_cat = {"size": "fat", "colour": "gray", "disposition": "loud"}
# print(my_cat["colour"])

# # Lists vs Dictionaries
# # lists: ordered, dict: unordered. Two dicts with different order but same values are equal.

# spam = ["cats", "dogs", "moose"]
# bacon = ["dogs", "moose", "cats"]
# print(spam == bacon)  # False

# eggs = {"name": "Zophie", "species": "cat", "age": "8"}
# ham = {"species": "cat", "age": "8", "name": "Zophie"}
# print(eggs == ham)  # True

# # KeyError: the key I'm trying to access does not exist
# # With dict you can organise data in powerful ways
# birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

# # keys(), values() and items()
# # items() returns tuples of the key and value
# # These functions return list-like values but not true lists
# # their data types are: dict_keys, dict_values, and dict_items
# # The values returned can not be modified and do not have an append() method
# # They can be used in for loops
# spam = {"colour": "red", "age": 42}
# for v in spam.values():
#     print(v)
# for k in spam.keys():
#     print(k)
# for i in spam.items():
#     print(i)

# # If I want a true list I can pass the result of the previous methods
# # to the list() function
# spam = {"colour": "red", "age": 42}
# print(spam.keys())
# print(list(spam.keys()))

# for k, v in spam.items():
#     print(f"Key: {k}, Value: {v}")

# # Checking if a key or a value exists in a dictionary

# spam = {"name": "Zophie", "age": 7}
# print("name" in spam.keys())
# print("Zophie" not in spam.values())
# print("name" in spam)  # when I'm looking for keys I can just write the dict name

# # get() -> .get(key_of_the_wanted_value, fallback_value)

# picnic_items = {"apples": 5, "cups": 2}
# print(
#     f"I'm bringing {str(picnic_items.get("cups", "no"))} cups "
#     f"and {str(picnic_items.get("eggs", "no"))} eggs."
#       )

# setdefault() -> setdefault(key_to_check, default_if_does_not_exist)
# sets a value in a dict key if it does not have one already
# works as a way to check if a key exists as well

spam = {"name": "Pooka", "age": 5}
print(spam.setdefault("color", "black"))
print(spam)
print(spam.setdefault("color", "white"))  # it already has a value, it won't change it
print(spam)
