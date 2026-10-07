import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "orders.json")


def load_orders():

    with open(FILE, "r") as file:
        return json.load(file)


def generate_bill():

    orders = load_orders()

    if not orders:
        print("No orders available.")
        return

    order_id = int(input("Enter order ID: "))

    for order in orders:

        if order["id"] == order_id:

            subtotal = order["total"]

            tax = subtotal * 0.05

            discount = 0

            if subtotal >= 1000:
                discount = subtotal * 0.10

            grand_total = subtotal + tax - discount

            print("\n================================")
            print("          HOTEL BILL")
            print("================================")

            print("Order ID :", order["id"])
            print("Customer :", order["customer"])
            print("Food     :", order["food"])
            print("Plate    :", order["plate"])
            print("Quantity :", order["quantity"])

            print("--------------------------------")

            print(f"Subtotal : ₹{subtotal:.2f}")
            print(f"Tax 5%   : ₹{tax:.2f}")
            print(f"Discount : ₹{discount:.2f}")

            print("--------------------------------")

            print(f"Total    : ₹{grand_total:.2f}")

            print("================================")

            return

    print("Order not found.")