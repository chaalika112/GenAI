class Store:
    def __init__(self):
        self.items = {
            "Apple": {"price": 2, "stock": 5},
            "Milk": {"price": 4, "stock": 3},
            "Bread": {"price": 3, "stock": 4},
            "Eggs": {"price": 5, "stock": 2}
        }

    def display_items(self):
        print("\nAvailabl Items:")
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

    def add_item(self, item_name):
        self.store.check_item(item_name)

        self.cart_items.append(item_name)
        self.store.items[item_name]["stock"] -= 1

        return item_name + " added to cart"

    def display_cart(self):
        if len(self.cart_items) == 0:
            return "Cart if empty"

        return self.cart_items

    def calculate_total(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += self.store.items[item]["price"]

        return total_cost