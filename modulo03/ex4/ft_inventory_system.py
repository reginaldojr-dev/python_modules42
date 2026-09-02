import sys


def parse_inventory(parameters: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for parameter in parameters:
        parts = parameter.split(":")

        if len(parts) != 2 or parts[0] == "" or parts[1] == "":
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item = parts[0]
        quantity_text = parts[1]

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_text)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    item_list = list(inventory.keys())
    quantities = list(inventory.values())
    total = sum(quantities)

    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} items: {total}")

    if total != 0:
        for item in item_list:
            percentage = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percentage}%")

    most_item = item_list[0]
    least_item = item_list[0]

    for item in item_list[1:]:
        if inventory[item] > inventory[most_item]:
            most_item = item
        if inventory[item] < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
