while True:
    name = input("who are you?")
    if name != "Joe":
        continue
    password = input("Hello, Joe. What is the password? (It is a fish.)")
    if password == "swordfish":
        break
print("Acccdess granted.")

print("My name is")
for i in range(5):
    print(f"Jimmy Five Times ({i})")

total = 0
finish = 100
for i in range(finish + 1):
    total += i
print(f"The sum of the numbers from 1 to {finish} is: {total}.")
