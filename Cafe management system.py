import datetime
import uuid
import os

menu = {
    'Pizza': {'price': 100, 'discount': 0},
    'Pasta': {'price': 80, 'discount': 0},
    'Burger': {'price': 60, 'discount': 10},
    'Salad': {'price': 50, 'discount': 0},
    'Coffee': {'price': 40, 'discount': 20}
}

loyalty_points = {}

# ---------------- ADMIN FEATURES ------------------
def admin_panel():
    while True:
        print("\n=== Admin Panel ===")
        print("1. View Menu")
        print("2. Add Item to Menu")
        print("3. Delete Item from Menu")
        print("4. Update Item Price")
        print("5. View Orders by Date")
        print("6. Exit Admin Panel")
        choice = input("Enter choice: ")

        if choice == '1':
            print("\nCurrent Menu:")
            for item, details in menu.items():
                print(f" - {item}: Rs{details['price']} (Discount: {details['discount']}%)")

        elif choice == '2':
            name = input("Enter new item name: ").title()
            price = int(input("Enter price: "))
            discount = int(input("Enter discount % (0 if none): "))
            menu[name] = {'price': price, 'discount': discount}
            print(f"{name} added to menu.")

        elif choice == '3':
            name = input("Enter item to remove: ").title()
            if name in menu:
                del menu[name]
                print(f"{name} removed.")
            else:
                print("Item not found.")

        elif choice == '4':
            name = input("Enter item to update: ").title()
            if name in menu:
                price = int(input("New price: "))
                discount = int(input("New discount %: "))
                menu[name] = {'price': price, 'discount': discount}
                print(f"{name} updated.")
            else:
                print("Item not found.")

        elif choice == '5':
            date_str = input("Enter date (YYYY-MM-DD): ")
            if os.path.exists("order_history.txt"):
                with open("order_history.txt", "r") as f:
                    print(f"\nOrders on {date_str}:")
                    lines = f.readlines()
                    found = False
                    for line in lines:
                        if date_str in line:
                            found = True
                            print(line.strip())
                    if not found:
                        print("No orders found for that date.")
            else:
                print("No order history found.")

        elif choice == '6':
            break
        else:
            print("Invalid choice.")

# ---------------- CUSTOMER ORDER ------------------
def take_order():
    print("\nWelcome to My Restaurant!")
    print("Here is our menu:")
    for item, info in menu.items():
        disc_info = f" (Discount: {info['discount']}%)" if info['discount'] > 0 else ""
        print(f" - {item}: Rs{info['price']}{disc_info}")

    name = input("\nEnter your name: ").strip().title()
    phone = input("Enter your mobile number: ").strip()
    bill_id = str(uuid.uuid4())[:8]  # Unique ID

    # Loyalty points
    previous_points = loyalty_points.get(phone, 0)
    print(f"Loyalty Points: {previous_points}")

    order_total = 0
    order_details = []

    while True:
        item = input("\nEnter the item name: ").strip().title()
        if item in menu:
            try:
                qty = int(input(f"Enter quantity for {item}: "))
                unit_price = menu[item]['price']
                discount = menu[item]['discount']
                discounted_price = unit_price * (1 - discount / 100)
                total_price = discounted_price * qty
                order_total += total_price
                order_details.append((item, qty, unit_price, discount, total_price))
                print(f"{qty} x {item} added.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Item not found.")

        more = input("Add another item? (yes/no): ").lower()
        if more != 'yes':
            break

    # Order discount if > 500
    additional_discount = 0
    if order_total > 500:
        additional_discount = 10
        order_total *= 0.90

    gst = order_total * 0.05
    grand_total = order_total + gst

    payment = input("Enter payment method (Cash/Card/UPI): ").title()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Loyalty point update (1 point per Rs. 100 spent)
    new_points = int(grand_total // 100)
    loyalty_points[phone] = previous_points + new_points

    # Print Bill
    print("\n========= Final Bill =========")
    print(f"Bill ID: {bill_id}")
    print(f"Customer: {name}")
    print(f"Mobile: {phone}")
    print(f"Time: {timestamp}")
    print(f"Payment: {payment}")
    print("-------------------------------")
    print(f"{'Item':10} {'Qty':>3} {'Rate':>5} {'Disc%':>6} {'Amount':>8}")
    print("-------------------------------")
    for item, qty, rate, disc, amount in order_details:
        print(f"{item:10} {qty:>3} {rate:>5} {disc:>6} {amount:>8.2f}")
    print("-------------------------------")
    if additional_discount:
        print("10% Discount applied on total")
    print(f"Subtotal: Rs {order_total:.2f}")
    print(f"GST (5%): Rs {gst:.2f}")
    print(f"Total Payable: Rs {grand_total:.2f}")
    print(f"Loyalty Points Earned: {new_points}")
    print("==============================")

    # Simulated Email Receipt
    print("\nSending bill to customer email (simulation)...")
    print("Receipt sent to registered mobile/email.")

    # Save to file
    with open("order_history.txt", "a") as f:
        f.write(f"\nBill ID: {bill_id}, Customer: {name}, Phone: {phone}, Time: {timestamp}, Payment: {payment}\n")
        for item, qty, rate, disc, amount in order_details:
            f.write(f"{item} x {qty} = Rs{amount:.2f} (Rate: {rate}, Discount: {disc}%)\n")
        if additional_discount:
            f.write("10% discount applied\n")
        f.write(f"Total: Rs {grand_total:.2f}, Loyalty Points: {new_points}\n")
        f.write("------------------------------------------\n")

# ---------------- ADMIN LOGIN FUNCTION ------------------
def admin_login():
    print("\n🔐 Admin Login")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    # Default admin credentials
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "1234"

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("✅ Login successful!\n")
        admin_panel()
    else:
        print("❌ Invalid credentials! Access Denied.")

# ---------------- MAIN APP ------------------
while True:
    print("\n===== Welcome =====")
    role = input("Are you a Customer or Admin? (C/A): ").strip().lower()

    if role == 'c':
        take_order()
    elif role == 'a':
        admin_login()   # ✅ call login before giving access
    else:
        print("Invalid role.")

    again = input("\nDo you want to restart the system? (Yes/No): ").strip().lower()
    if again != 'yes':
        print("Goodbye!")
        break
