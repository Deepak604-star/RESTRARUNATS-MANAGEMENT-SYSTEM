import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "inventory.json")


def load_inventory():

    if not os.path.exists(FILE):

        data = [
            {
                "id": 1,
                "item": "Rice",
                "quantity": 50,
                "unit": "kg"
            },
            {
                "id": 2,
                "item": "Paneer",
                "quantity": 20,
                "unit": "kg"
            },
            {
                "id": 3,
                "item": "Chicken",
                "quantity": 30,
                "unit": "kg"
            },
            {
                "id": 4,
                "item": "Oil",
                "quantity": 25,
                "unit": "litre"
            }
        ]

        save_inventory(data)

    with open(FILE, "r") as file:
        return json.load(file)


def save_inventory(data):

    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)


def show_inventory():

    inventory = load_inventory()

    print("\n========== INVENTORY ==========")

    for item in inventory:

        print(
            f"ID: {item['id']} | "
            f"{item['item']} | "
            f"{item['quantity']} {item['unit']}"
        )


def add_stock():

    inventory = load_inventory()

    item = input("Please enter the item name: ")
    quantity = float(input("Please enter the quantity: "))
    unit = input("Please enter the unit: ")

    new_id = max([x["id"] for x in inventory],  default=0  ) + 1

    inventory.append({
        "id": new_id,
        "item": item,
        "quantity": quantity,
        "unit": unit
    })

    save_inventory(inventory)

    print("Stock added successfully.")


def update_stock():

    inventory = load_inventory()

    show_inventory()

    item_id = int(input("\nPlease enter item ID: "))

    for item in inventory:

        if item["id"] == item_id:

            item["quantity"] = float(input("Pleasee enter new quantity: "))

            save_inventory(inventory)

            print("Stock updated successfully.")
            return

    print("Item not found.")