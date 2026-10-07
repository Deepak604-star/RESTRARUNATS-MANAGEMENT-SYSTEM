import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "menu.json")


def load_menu():

    if not os.path.exists(FILE):

        data = [
            {
                "id": 1,
                "name": "Paneer Butter Masala",
                "category": "North Indian",
                "half_price": 120,
                "full_price": 220
            },
            {
                "id": 2,
                "name": "Dal Makhani",
                "category": "North Indian",
                "half_price": 100,
                "full_price": 180
            },
            {
                "id": 3,
                "name": "Veg Biryani",
                "category": "Rice",
                "half_price": 100,
                "full_price": 180
            },
            {
                "id": 4,
                "name": "Chicken Biryani",
                "category": "Non-Veg",
                "half_price": 150,
                "full_price": 280
            },
            {
                "id": 5,
                "name": "Masala Dosa",
                "category": "South Indian",
                "half_price": 70,
                "full_price": 120
            },
            {
                "id": 6,
                "name": "Paneer Tikka",
                "category": "Starter",
                "half_price": 140,
                "full_price": 250
            },
            {
                "id": 7,
                "name": "Butter Naan",
                "category": "Bread",
                "half_price": 40,
                "full_price": 70
            },
            {
                "id": 8,
                "name": "Cold Coffee",
                "category": "Beverage",
                "half_price": 80,
                "full_price": 120
            }
        ]

        save_menu(data)

    with open(FILE, "r") as file:
        return json.load(file)


def save_menu(menu):

    with open(FILE, "w") as file:
        json.dump(menu, file, indent=4)


def show_menu():

    menu = load_menu()

    print("\n================ MENU ================")

    print(
        f"{'ID':<5}"
        f"{'Food':<25}"
        f"{'Category':<18}"
        f"{'Half':<10}"
        f"{'Full':<10}"
    )

    print("-" * 68)

    for food in menu:

        print(
            f"{food['id']:<5}"
            f"{food['name']:<25}"
            f"{food['category']:<18}"
            f"₹{food['half_price']:<9}"
            f"₹{food['full_price']}"
        )


def add_food():

    menu = load_menu()

    print("\n========== ADD FOOD ==========")

    name = input("Please enter the food name: ")
    category = input("Please enetr the Category: ")

    half_price = float(input("Half plate price: "))
    full_price = float(input("Full plate price: "))

    new_id = max([food["id"] for food in menu], default=0) + 1

    menu.append({
        "id": new_id,
        "name": name,
        "category": category,
        "half_price": half_price,
        "full_price": full_price
    })

    save_menu(menu)

    print("Food added successfully.")


def update_food():

    menu = load_menu()

    show_menu()

    food_id = int(input("\n Please enter the food ID: "))

    for food in menu:

        if food["id"] == food_id:

            food["name"] = input("Please enter the new food name: ")
            food["category"] = input("Please enter the new category: ")
            food["half_price"] = float(input("Please enter the new half price: "))
            food["full_price"] = float(input("Please enter the new full price: "))

            save_menu(menu)

            print("Food updated successfully.")
            return

    print("Food not found.")


def delete_food():

    menu = load_menu()

    show_menu()

    food_id = int(input("\nPlease enter the food ID: "))

    new_menu = [food for food in menu if food["id"] != food_id]

    if len(new_menu) == len(menu):
        print("Food not found.")
        return

    save_menu(new_menu)

    print("Food deleted successfully.")