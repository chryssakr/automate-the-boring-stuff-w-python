def list_items(my_list: list) -> str:
    if len(my_list) > 1:
        reply = ", ".join(my_list[:-1]) + " and " + my_list[-1]
    elif len(my_list) == 1:
        reply = my_list[0]
    else:
        reply = ""
    return reply

spam = ["apples", "bananas", "tofu", "cats"]
print(list_items(spam))