import sys

while True:
    response = input("Type exit to exit.\n")
    if response == "exit":
        sys.exit()
    print(f"You typed: {response}")
