class Store:
    def __init__(self):
        self.items = {
            "Apple": {"price": 2, "stock": 5},
            "Milk": {"price": 4, "stock": 3},
            "Bread": {"price": 3, "stock": 4},
            "Eggs": {"price": 5, "stock": 2}
        }

    def display_items(self):
        print("\nAvailable Items:")
        for item, details in self.items.items():
            print(item, "- Price:", details["price"], "- Stock:", details["stock"])

    def check_item(self, item_name):
        if item_name not in self.items:
            raise ValueError("Item not found")

        if self.items[item_name]["stock"] <= 0:
            raise ValueError("Item is out of stock")


class Cart:
    def __init__(self, store):
        self.store = store
        self.cart_items = []

    def add_item(self, item_name, quantity):

        self.store.check_item(item_name)

        stock = self.store.items[item_name]["stock"]

        if quantity > stock:
           raise ValueError("Only " + str(stock) + " items available")

        for i in range(quantity):
           self.cart_items.append(item_name)

        self.store.items[item_name]["stock"] -= quantity

        return item_name + " added to cart"

    def display_cart(self):

        if len(self.cart_items) == 0:
            return "\nCart is empty"

        result = []

        for item in self.store.items:

            quantity = self.cart_items.count(item)

            if quantity > 0:
                result.append(item + " - " + str(quantity))

        return result
            
    def calculate_total(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += self.store.items[item]["price"]

        return total_cost
    def remove_item(self, item_name, quantity):

        if item_name not in self.cart_items:
            raise ValueError("Item not found in cart")

        cart_quantity = self.cart_items.count(item_name)

        if quantity > cart_quantity:
            raise ValueError("You only have " + str(cart_quantity) + " " + item_name + " in cart")

        for i in range(quantity):
            self.cart_items.remove(item_name)

        self.store.items[item_name]["stock"] += quantity

        return item_name + " removed from cart"

