while True:
    name = input('who are you?')
    if name != 'Joe':
        continue
    password = input('Hello, Joe. What is the password? (It is a fish.)')
    if password == 'swordfish':
        break
print('Access granted.')

print('My name is')
for i in range(5):
    print(f'Jimmy ({i})')
