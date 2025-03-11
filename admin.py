MENU_FILE = "menu.txt"

class Admin:
    def __init__(self):
        self.admin_username = "amar"
        self.admin_password = "amar@29"

    def login(self, username, password):
        try:
            if username == self.admin_username and password == self.admin_password:
                print("Login successful!")
                return True
            else:
                print("Incorrect Password")
                return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def admin_menu(self, customer):
        while True:
            try:
                print("\n--- Admin Menu ---")
                print("1. Add Item to Menu")
                print("2. Show Menu")
                print("3. View Registered Customers")
                print("4. View All Customer Orders")
                print("5. Log Out")

                choice = input("Enter your choice: ")

                if choice == "1":
                    item = input("Enter the item name to add: ")
                    price = input("Enter the price for the item: ")
                    self.add_item(item, price)
                elif choice == "2":
                    self.view_menu()
                elif choice == "3":
                    customer.count_registered_customers()
                elif choice == "4":
                    customer.view_all_customers_orders()
                elif choice == "5":
                    print("You are Logged out")
                    break  
                else:
                    print("Invalid choice...Please try again.")
            except Exception as e:
                print(f"Error in admin menu: {e}")

    def add_item(self, item, price):
        try:
            with open(MENU_FILE, "a") as f:
                f.write(f"{item},{price}\n")
            print(f"{item} added to the menu.")
        except Exception as e:
            print(f"Error adding item: {e}")

    def view_menu(self):
        try:
            print("\n--- Menu ---")
            with open(MENU_FILE, "r") as f:
                menu_items = f.read()

            if menu_items:
                lines = menu_items.split("\n")
                for line in lines:
                    if line:
                        item, price = line.split(",")
                        print(f"{item} - Rs.{price}")
            else:
                print("Menu is empty!")
        except Exception as e:
            print(f"Error viewing menu: {e}")
