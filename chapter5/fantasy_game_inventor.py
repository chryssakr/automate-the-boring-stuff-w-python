def display_inventory(inventory: dict) -> None:
    print("-----------Inventory----------")
    total_items = sum(inventory.values())
    for k, v in inventory.items():
        print(f"{v}\t{k}")
    print(
        "------------------------------\n" f"Total number of items: {str(total_items)}"
    )


def add_to_inventory(inventory: dict, items_to_add: list) -> dict:
    for item in items_to_add:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def main():
    inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
    display_inventory(inventory)
    dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
    updated_inventory = add_to_inventory(inventory, dragon_loot)
    display_inventory(updated_inventory)


if __name__ == "__main__":
    main()
