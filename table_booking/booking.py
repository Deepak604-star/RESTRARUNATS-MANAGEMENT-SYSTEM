import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, "data", "tables.json")


def load_tables():

    if not os.path.exists(FILE):

        data = [
            {
                "id": 1,
                "category": "Small",
                "seats": 2,
                "bookings": []
            },
            {
                "id": 2,
                "category": "Medium",
                "seats": 4,
                "bookings": []
            },
            {
                "id": 3,
                "category": "Large",
                "seats": 6,
                "bookings": []
            },
            {
                "id": 4,
                "category": "VIP",
                "seats": 8,
                "bookings": []
            },
            {
                "id": 5,
                "category": "Small",
                "seats": 2,
                "bookings": []
            }
        ]

        save_tables(data)

    with open(FILE, "r") as file:
        return json.load(file)


def save_tables(tables):

    with open(FILE, "w") as file:
        json.dump(tables, file, indent=4)


def show_tables():

    tables = load_tables()

    print("\n================ TABLES ================")

    for table in tables:

        print(f"\nTable ID : {table['id']}")

        print( f"Category : {table['category']}")

        print( f"Seats : {table['seats']}")

        if not table["bookings"]:

            print("Status   : Available")

        else:

            print("Bookings:")

            for booking in table["bookings"]:

                print( f"  Customer : {booking['customer']}" )

                print( f"  Date  : {booking['date']}")

                print(f"  Time  : {booking['start_time']}")

                print( f"  End Time : {booking['end_time']}")


def book_table():

    tables = load_tables()

    print("\n========== BOOK TABLE ==========")

    customer = input("Customer name: ")

    show_tables()

    table_id = int(input("\nPlease enter the table ID: "))

    selected_table = None

    for table in tables:

        if table["id"] == table_id:
            selected_table = table
            break

    if selected_table is None:

        print("Table not found.")
        return

    date = input( "Booking date (YYYY-MM-DD): ")

    time = input("Booking time (HH:MM): ")

    duration = int( input("Duration in hours: "))

    try:

        start = datetime.strptime( f"{date} {time}", "%Y-%m-%d %H:%M")

    except ValueError:

        print("Invalid date or time format.")
        return

    end = start + timedelta(hours=duration)

    for booking in selected_table["bookings"]:

        old_start = datetime.strptime( f"{booking['date']} {booking['start_time']}", "%Y-%m-%d %H:%M")

        old_end = datetime.strptime(f"{booking['date']} {booking['end_time']}", "%Y-%m-%d %H:%M" )

        if start < old_end and end > old_start:

            print( "This table is already booked ""for this time." )

            return

    selected_table["bookings"].append({

        "customer": customer,

        "date": date,

        "start_time": start.strftime("%H:%M"),

        "end_time": end.strftime("%H:%M"),

        "duration": duration
    })

    save_tables(tables)

    print("\nTable booked successfully.")

    print("Table     :", selected_table["id"])
    print("Category  :", selected_table["category"])
    print("Customer  :", customer)
    print("Date      :", date)
    print("Start     :", start.strftime("%H:%M"))
    print("End       :", end.strftime("%H:%M"))


def cancel_table():

    tables = load_tables()

    show_tables()

    table_id = int(input("\nPlease enter the table ID: "))

    date = input( "Please enter the booking date (YYYY-MM-DD): " )

    time = input("Please enter the booking time (HH:MM): ")

    for table in tables:

        if table["id"] == table_id:

            for booking in table["bookings"]:

                if (
                    booking["date"] == date
                    and booking["start_time"] == time
                ):

                    table["bookings"].remove(booking)

                    save_tables(tables)

                    print( "Table booking cancelled." )

                    return

    print("Booking not found.")