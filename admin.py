MENU_FILE = "menu.txt"

class Admin:
    def __init__(self):
        self.admin_username = "amar"
        self.admin_password = "amar@29"

    def login(self, username, password):
        if username == self.admin_username and password == self.admin_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect Password")
            return False

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Item to Menu")
            print("2. Show Menu")
            print("3. Log Out")

            choice = input("Enter your choice: ")

            if choice == "1":
                item = input("Enter the item name to add: ")
                price = input("Enter the price for the item: ")
                self.add_item(item, price)
            elif choice == "2":
                self.view_menu()
            elif choice == "3":
                print("You are Logged out")
                break  
            else:
                print("Invalid choice...Please try again.")

    def add_item(self, item, price):
        with open(MENU_FILE, "r") as f:
            menu_items = f.read()

        lines = menu_items.split("\n")
        for line in lines:
            if line:
                existing_item, _ = line.split(",")
                if item.lower() == existing_item.lower():
                    print(f"{item} is already in the menu.")
                    return
        
        # Add new item to the menu
        with open(MENU_FILE, "a") as f:
            f.write(f"{item},{price}\n")
        print(f"{item} added to the menu.")

    def view_menu(self):
        print("\n--- Menu ---")
        with open(MENU_FILE, "r") as f:
            menu_items = f.read()

        if menu_items:
            lines = menu_items.split("\n")
            for line in lines:
                if line:
                    item, price = line.split(",")
                    print(f"{item} - ${price}")
        else:
            print("Menu is empty!")
