import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

FILE = os.path.join(DATA_DIR, "users.json")

def load_users():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(FILE):

        with open(FILE, "w") as file:
            json.dump([], file, indent=4)

    with open(FILE, "r") as file:
        return json.load(file)

def save_users(users):

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)


def signup():

    users = load_users()

    print("\n==============================")
    print("          SIGN UP")
    print("==============================")

    username = input("Please enter the username: ").strip()
    password = input("Please enter the password: ").strip()

    if username == "" or password == "":
        print("Username and password cannot be empty.")
        return


    for user in users:

        if user["username"] == username:

            print("Username already exists.")
            return

    print("\nSelect Role")
    print("1. Admin")
    print("2. Staff")

    role_choice = input("Please enter the choice: ").strip()

    if role_choice == "1":

        role = "Admin"

    elif role_choice == "2":

        role = "Staff"

    else:

        print("Invalid role.")
        return

    new_user = {
        "username": username,
        "password": password,
        "role": role
    }

    users.append(new_user)

    save_users(users)

    print("\nSignup successful.")
    print("Username:", username)
    print("Role:", role)


def login():

    users = load_users()

    print("\n==============================")
    print("           LOGIN")
    print("==============================")

    username = input("Please enter the username: ").strip()
    password = input("Please enter the password: ").strip()

    for user in users:

        if (
            user["username"] == username
            and user["password"] == password
        ):

            print("\nLogin successful.")
            print("Welcome:", username)
            print("Role:", user["role"])

            return user["role"]

    print("\nInvalid username or password.")

    return None

def admin_menu():

    from menu.menu import (
        show_menu,
        add_food,
        update_food,
        delete_food
    )

    from inventory.inventory import (
        show_inventory,
        add_stock,
        update_stock
    )

    from orders.order import (
        create_order,
        show_orders,
        update_order,
        cancel_order
    )

    from billing.bill import generate_bill

    from table_booking.booking import (
        show_tables,
        book_table,
        cancel_table
    )

    while True:

        print("\n================================")
        print("          ADMIN MENU")
        print("================================")

        print("1. Show Menu")
        print("2. Add Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Create Order")
        print("6. Show Orders")
        print("7. Update Order")
        print("8. Cancel Order")
        print("9. Generate Bill")
        print("10. Show Inventory")
        print("11. Add Stock")
        print("12. Update Stock")
        print("13. Show Tables")
        print("14. Book Table")
        print("15. Cancel Table")
        print("16. Logout")

        choice = input("Please enter the choice: ").strip()

        if choice == "1":

            show_menu()

        elif choice == "2":

            add_food()

        elif choice == "3":

            update_food()

        elif choice == "4":

            delete_food()

        elif choice == "5":

            create_order()

        elif choice == "6":

            show_orders()

        elif choice == "7":

            update_order()

        elif choice == "8":

            cancel_order()

        elif choice == "9":

            generate_bill()

        elif choice == "10":

            show_inventory()

        elif choice == "11":

            add_stock()

        elif choice == "12":

            update_stock()

        elif choice == "13":

            show_tables()

        elif choice == "14":

            book_table()

        elif choice == "15":

            cancel_table()

        elif choice == "16":

            print("Admin logged out.")
            break

        else:

            print("Invalid choice.")

def staff_menu():

    from menu.menu import show_menu

    from orders.order import (
        create_order,
        show_orders,
        update_order,
        cancel_order
    )

    from billing.bill import generate_bill

    from inventory.inventory import show_inventory

    from table_booking.booking import (
        show_tables,
        book_table,
        cancel_table
    )

    while True:

        print("\n================================")
        print("          STAFF MENU")
        print("================================")

        print("1. Show Menu")
        print("2. Create Order")
        print("3. Show Orders")
        print("4. Update Order")
        print("5. Cancel Order")
        print("6. Generate Bill")
        print("7. Show Inventory")
        print("8. Show Tables")
        print("9. Book Table")
        print("10. Cancel Table")
        print("11. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":

            show_menu()

        elif choice == "2":

            create_order()

        elif choice == "3":

            show_orders()

        elif choice == "4":

            update_order()

        elif choice == "5":

            cancel_order()

        elif choice == "6":

            generate_bill()

        elif choice == "7":

            show_inventory()

        elif choice == "8":

            show_tables()

        elif choice == "9":

            book_table()

        elif choice == "10":

            cancel_table()

        elif choice == "11":

            print("Staff logged out.")
            break

        else:

            print("Invalid choice.")

def start():

    while True:

        print("\n================================")
        print("       HOTEL MANAGEMENT SYSTEM")
        print("================================")

        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Please enter the choice: ").strip()

        if choice == "1":

            signup()

        elif choice == "2":

            role = login()

            if role == "Admin":

                admin_menu()

            elif role == "Staff":

                staff_menu()

        elif choice == "3":

            print("\nThank you for using Hotel Management System.")
            break

        else:

            print("Invalid choice.")