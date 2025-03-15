Overview:-
This is a Restaurant Management System implemented using Object-Oriented Programming (OOP) concepts in Python. 
The system includes functionalities for both admin and customers while utilizing file handling and try-except blocks for data management and error handling.
Features:-
1. Admin Module (admin.py)
Admin can log in using credentials.
View the restaurant menu.
Add or delete food items from the menu.
Check the number of registered customers.
View customer orders.
2. Customer Module (customer.py)
Customers can register with a name and password.
Customers can log in using their credentials.
View the restaurant menu.
Place multiple food orders at a time.
See their ordered food along with costs.
3.Menu Module(menu.pu)
Key Improvements:-
Dynamic Menu Display
Instead of hardcoding the menu, it now reads items from menu.txt and displays them dynamically.
File Handling Best Practices:
Ensures the file exists before reading/writing.
Error Handling & Edge Cases:
Displays a message if the menu is empty.
Handles cases where an item already exists.
Main Block for Testing:
Running menu.py directly will now display the menu.
4.Order Module(order.py
Placing an Order – Customers select food items from the menu.
Storing Orders – Orders are saved in orders.txt.
Viewing Orders – Admin can check customer orders.
