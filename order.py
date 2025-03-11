MENU_FILE = "menu.txt"

class Menu:
    def __init__(self):
        try:
            open(MENU_FILE, "a").close()
        except Exception as e:
            print(f"Error initializing menu file: {e}")

    def add_item(self, item, price):
        try:
            with open(MENU_FILE, "r") as f:
                menu_items = f.read()

            lines = menu_items.split("\n")  
            for line in lines:
                if line: 
                    existing_item, _ = line.split(",")
                    if item.lower() == existing_item.lower(): 
                        print(f"{item} is already in the menu.")
                        return

            with open(MENU_FILE, "a") as f:
                f.write(f"{item},{price}\n")
            print(f"{item} added to the menu.")
        except Exception as e:
            print(f"Error adding item to menu: {e}")

    def view_menu(self):
        try:
            print("\n--- Menu ---\n1. Fried Rice \n2. French Fries \n3. Pizza \n4. Burger ")
            print("\n--- Cold Drinks ---\na. Sprite \nb. Maaza \nc. Coke ")
        except Exception as e:
            print(f"Error displaying menu: {e}")
