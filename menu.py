MENU_FILE = "menu.txt"

class Menu:
    def __init__(self):
        open(MENU_FILE, "a").close()  # Ensure the file exists by opening it in append mode

    def add_item(self, item, price):
        # Read current menu items
        with open(MENU_FILE, "r") as f:
            menu_items = f.read()

        # Check if the item already exists in the file
        lines = menu_items.split("\n")  # Split content by new line
        for line in lines:
            if line:  # Check if line is not empty
                existing_item, _ = line.split(",")
                if item.lower() == existing_item.lower():  # Case-insensitive check
                    print(f"{item} is already in the menu.")
                    return

        # If item doesn't exist, append it to the menu
        with open(MENU_FILE, "a") as f:
            f.write(f"{item},{price}\n")
        print(f"{item} added to the menu.")

    def view_menu(self):
        print("\n---Menu---\n1.Fried Rice \n2.Frenchfries \n3.Pizza \n4.Burger ")
    
        print("\n---Coldrinks---\na.Sprite \nb.Maza \nc.Cock ")
