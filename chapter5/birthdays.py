birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}
while True:
    name = input("Enter a name: (blank to quit)")
    if name == "":
        break
    if name in birthdays:  # checks if name is a key in the dict
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I don't have birthday information for {name}")
        bday = input("What is their birthday?")
        birthdays[name] = bday
        print("Birthday database updated!")
