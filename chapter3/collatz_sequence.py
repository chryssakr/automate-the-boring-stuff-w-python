def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


user_input = input("Give a number: ")
try:
    int_input = int(user_input)
    sequenced = collatz(user_input)
    while sequenced != 1:
        sequenced = collatz(sequenced)
except ValueError:
    print("Enter an integer please")
