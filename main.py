from admin import Admin
from menu import Menu
from order import Order
from customerlogin import Customer

def main():
    admin = Admin()
    menu = Menu()
    order = Order()
    customer = Customer()

    logged_in_customer = None
    is_admin_logged_in = False

    while True:
        try:
            print("\n--- Restaurant Management System ---")
            print("1. Admin Login")
            print("2. Customer Register")
            print("3. Customer Login")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                if admin.login(username, password):
                    is_admin_logged_in = True
                    while True:
                        print("\n--- Admin Menu ---")
                        print("1. Add Item to Menu")
                        print("2. Show Menu")
                        print("3. View Registered Customers")
                        print("4. View All Customer Orders")
                        print("5. Log Out")

                        admin_choice = input("Enter your choice: ")
                        
                        if admin_choice == "1":
                            item = input("Enter item name: ")
                            price = input("Enter item price: ")
                            admin.add_item(item, price)
                        elif admin_choice == "2":
                            menu.view_menu()
                        elif admin_choice == "3":
                            customer.count_registered_customers()
                        elif admin_choice == "4":
                            customer.view_all_customers_orders()
                        elif admin_choice == "5":
                            print("Logging out...")
                            is_admin_logged_in = False
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                customer.register(username, password)
            elif choice == "3":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if customer.login(username, password):
                    print("Customer login successful!")
                    logged_in_customer = Customer()
                    logged_in_customer.username = username
                    
                    while True:
                        print("\n--- Customer Menu ---")
                        print("1. View Menu")
                        print("2. Place Order")
                        print("3. View Orders")
                        print("4. Logout")

                        customer_choice = input("Enter your choice: ")

                        if customer_choice == "1":
                            menu.view_menu()
                        elif customer_choice == "2":
                            logged_in_customer.place_order()
                        elif customer_choice == "3":
                            logged_in_customer.view_orders()
                        elif customer_choice == "4":
                            print("Logging out...")
                            logged_in_customer = None
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == "4":
                print("Exiting..Thank you!")
                break
            else:
                print("Invalid choice or unauthorized access. Please try again.")
        except Exception as e:
            print(f"Error in main menu: {e}")

if __name__ == "__main__":
    main()
