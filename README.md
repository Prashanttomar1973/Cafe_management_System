☕ Cafe Management System - Python CLI Project
A simple command-line-based Cafe Management System developed in Python. This project helps manage orders, generate bills, track customer loyalty points, and allows admin-level menu management.

📌 Features
👤 Customer Side
View menu with discounts
Place orders with quantity
Automatic bill generation with:
Subtotal
GST (5%)
Additional discount if order > ₹500
Loyalty Points system (1 point per ₹100 spent)
Receipt saved to order_history.txt
Simulated bill sending via email
🔐 Admin Side
Admin login (username: admin, password: 1234)
Add, delete or update menu items
View current menu
View past orders by date (search in order_history.txt)
📁 Folder Structure
CafeManagementSystem/
├── main.py                # Main Python file
├── order_history.txt      # Auto-generated file to store orders
├── README.md              # This file
🚀 How to Run
▶️ Run in CMD / Terminal
python main.py
Make sure you have Python 3 installed.

🧠 Technologies Used
Python 3
datetime, uuid, os modules (built-in)
No external libraries required
📸 Sample Output
===== Welcome =====
Are you a Customer or Admin? (C/A): c

Welcome to My Restaurant!
Here is our menu:
 - Pizza: Rs100
 - Pasta: Rs80
 - Burger: Rs60 (Discount: 10%)
 - Salad: Rs50
 - Coffee: Rs40 (Discount: 20%)

Enter your name: Rohan
Enter your mobile number: 9876543210
Loyalty Points: 10

Enter the item name: Pizza
Enter quantity for Pizza: 2
2 x Pizza added.

...

========= Final Bill =========
Bill ID: 9f5c2f1e
Customer: Rohan
Mobile: 9876543210
Payment: UPI
Subtotal: Rs 180.00
GST (5%): Rs 9.00
Total Payable: Rs 189.00
Loyalty Points Earned: 1
🧾 Sample Admin Panel
=== Admin Panel ===
1. View Menu
2. Add Item to Menu
3. Delete Item from Menu
4. Update Item Price
5. View Orders by Date
6. Exit Admin Panel
🔐 Default Admin Login
Username: admin
Password: 1234
You can modify these in the code for security.

✍️ Author
Prashant Tomar
🔗 GitHub: @Prashanttomar1973
⚠️ Disclaimer
This is a CLI-based educational project. For real-world cafe systems, consider adding:

GUI with Tkinter or PyQt
PDF bill generation
Database (e.g., SQLite/MySQL) for storing users & orders
Admin password hashing
📄 License
This project is licensed under the MIT License.

⭐ Like this project?
Please ⭐ star the repo and share with your peers!
