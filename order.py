MENU_FILE = "menu.txt"
ORDER_FILE = "orders.txt"

class Order:
    def __init__(self):
        self.orders = [] 

    def place_order(self, item, quantity):
        with open(MENU_FILE, "r") as f:
            menu_items = f.read()

        lines = menu_items.split("\n")
        for line in lines:
            if line:
                existing_item, price = line.split(",")
                if item.lower() == existing_item.lower():
                   
                    total_price = float(price) * quantity
               
                    self.orders.append({"item": item, "quantity": quantity, "price": float(price), "total": total_price})
                    print(f"Order placed for {quantity} x {item} at ${price} each. Total: ${total_price}")
                    return
        print(f"{item} is not available in the menu.")  

    def view_orders(self):
        if not self.orders:
            print("No orders placed yet.")
        else:
            print("\n--- Orders ---")
            total_amount = 0
            for order in self.orders:
                print(f"{order['quantity']} x {order['item']} - ${order['total']}")
                total_amount += order['total']
            print(f"Total: ${total_amount}")
