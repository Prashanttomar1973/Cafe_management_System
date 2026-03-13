☕ Cafe Management System - Python CLI Project

A simple command-line-based Cafe Management System developed in Python. This project helps manage orders, generate bills, track customer loyalty points, and allows admin-level menu management.

📌 Features

👤 Customer Side

View Menu: See available items with active discounts.

Place Orders: Order multiple items with specific quantities.

Automatic Bill Generation: Includes:

Subtotal calculation

GST (5%)

Additional discount for orders > ₹500

Loyalty Points System: Earn 1 point per ₹100 spent.

Receipt Storage: Orders are automatically saved to order_history.txt.

Email Simulation: Simulated notification sent upon order completion.

🔐 Admin Side

Admin Login: Secured access (Username: admin, Password: 1234).

Menu Management: Add, delete, or update menu items and prices.

View Menu: Real-time view of the current offerings.

Order Tracking: View past orders by date or search the history file.

📁 Folder Structure

CafeManagementSystem/
├── main.py              # Main Python logic file
├── order_history.txt    # Auto-generated file to store orders
└── README.md            # Project documentation (this file)


🚀 How to Run

Ensure you have Python 3 installed on your system.

Open your CMD, Terminal, or PowerShell.

Navigate to the project folder.

Run the following command:

python main.py


🧠 Technologies Used

Language: Python 3

Modules: datetime, uuid, os (All built-in)

Requirements: No external libraries required.

📸 Sample Output

Customer Interface:

===== Welcome =====
Are you a Customer or Admin? (C/A): c

Welcome to My Restaurant! Here is our menu:

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


Final Bill Example:

========= Final Bill =========
Bill ID: 9f5c2f1e
Customer: Rohan
Mobile: 9876543210
Payment: UPI
Subtotal: Rs 180.00
GST (5%): Rs 9.00
Total Payable: Rs 189.00
Loyalty Points Earned: 1


🧾 Admin Panel:

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
(Note: You can modify these values in the source code for better security.)

✍️ Author

Prashant Tomar 🔗 GitHub: @Prashanttomar1973

⚠️ Disclaimer

This is a CLI-based educational project. For real-world production systems, consider adding:

GUI using Tkinter or PyQt.

PDF bill generation.

Database (SQLite/MySQL) for persistent user and order storage.

Password hashing for admin security.

📄 License

This project is licensed under the MIT License.

⭐ Like this project? Please star the repo and share it with your peers!
