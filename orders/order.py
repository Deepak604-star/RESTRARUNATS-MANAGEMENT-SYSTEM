import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "orders.json")


def load_orders():

    if not os.path.exists(FILE):

        with open(FILE, "w") as file:
            json.dump([], file, indent=4)

    with open(FILE, "r") as file:
        return json.load(file)


def save_orders(orders):

    with open(FILE, "w") as file:
        json.dump(orders, file, indent=4)


def create_order():

    from menu.menu import load_menu

    menu = load_menu()

    show_menu_data(menu)

    orders = load_orders()

    order_id = max([order["id"] for order in orders], default=0 ) + 1

    customer = input("\nPlease enter the Customer name: ")

    food_id = int(input("Please enter the food ID: "))

    selected_food = None

    for food in menu:

        if food["id"] == food_id:
            selected_food = food
            break

    if selected_food is None:
        print("Food not found.")
        return

    print("1. Half")
    print("2. Full")

    plate = input("Please select the plate: ")

    if plate == "1":
        plate_type = "Half"
        price = selected_food["half_price"]

    elif plate == "2":
        plate_type = "Full"
        price = selected_food["full_price"]

    else:
        print("Invalid plate.")
        return

    quantity = int(input("Quantity: "))

    total = price * quantity

    order = {
        "id": order_id,
        "customer": customer,
        "food": selected_food["name"],
        "plate": plate_type,
        "quantity": quantity,
        "price": price,
        "total": total,
        "status": "Active",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M")
    }

    orders.append(order)

    save_orders(orders)

    print("\nOrder created successfully.")
    print("Order ID:", order_id)
    print("Total:", total)


def show_menu_data(menu):

    print("\n========== MENU ==========")

    for food in menu:

        print(
            food["id"],
            food["name"],
            "- Half ₹",
            food["half_price"],
            "| Full ₹",
            food["full_price"]
        )


def show_orders():

    orders = load_orders()

    print("\n========== ORDERS ==========")

    if not orders:
        print("No orders found.")
        return

    for order in orders:

        print(
            f"ID: {order['id']} | "
            f"Customer: {order['customer']} | "
            f"Food: {order['food']} | "
            f"{order['plate']} | "
            f"Qty: {order['quantity']} | "
            f"Total: ₹{order['total']} | "
            f"Status: {order['status']} | "
            f"{order['date']} {order['time']}"
        )


def update_order():

    orders = load_orders()

    show_orders()

    order_id = int(input("\nPlease enter the order ID: "))

    for order in orders:

        if order["id"] == order_id:

            order["quantity"] = int(input("Please enter the new quantity: "))

            order["total"] = (order["price"] * order["quantity"])

            save_orders(orders)

            print("Order updated successfully.")
            return

    print("Order not found.")


def cancel_order():

    orders = load_orders()

    show_orders()

    order_id = int(input("\nPlease enter the order ID: "))

    for order in orders:

        if order["id"] == order_id:

            order["status"] = "Cancelled"

            save_orders(orders)

            print("Order cancelled successfully.")
            return

    print("Order not found.")