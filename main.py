from menu import Menu
from order import Order
from admin import Admin

def main():
    menu = Menu()
    admin = Admin()
    order = Order()

    while True:
        print("\n1. Admin Login")
        print("2. View Menu")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if admin.login(username, password):
                print("Welcome, admin!")
                admin.admin_menu()
        elif choice == "2":
            menu.view_menu()
        elif choice == "3":
            item = input("Enter item to order: ")
            quantity = int(input("Enter quantity: "))
            order.place_order(item, quantity)
        elif choice == "4":
            order.view_orders()
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice")


main()
