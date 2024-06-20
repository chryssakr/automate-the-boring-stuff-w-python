def display_inventory(inventory: dict) -> None:
    print("-----------Inventory----------")
    total_items = sum(inventory.values())
    for k, v in inventory.items():
        print(f"{v}\t{k}")
    print(
        "------------------------------\n" f"Total number of items: {str(total_items)}"
    )


def main():
    inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    display_inventory(inventory)


if __name__ == "__main__":
    main()
