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


class AddItem:
    def add_item(self, cart, item_name, quantity):
        cart.store.check_item(item_name)

        stock = cart.store.items[item_name]["stock"]

        if quantity > stock:
            raise ValueError("Only " + str(stock) + " items available")

        for i in range(quantity):
            cart.cart_items.append(item_name)

        cart.store.items[item_name]["stock"] -= quantity

        return item_name + " added to cart"


class DisplayCart:
    def display_cart(self, cart):
        if len(cart.cart_items) == 0:
            return "\nCart is empty"

        result = []

        for item in cart.store.items:
            quantity = cart.cart_items.count(item)

            if quantity > 0:
                result.append(item + " - " + str(quantity))

        return result


class CalculateTotal:
    def calculate_total(self, cart):
        total_cost = 0

        for item in cart.cart_items:
            total_cost += cart.store.items[item]["price"]

        return total_cost


class RemoveItem:
    def remove_item(self, cart, item_name, quantity):
        if item_name not in cart.cart_items:
            raise ValueError("Item not found in cart")

        cart_quantity = cart.cart_items.count(item_name)

        if quantity > cart_quantity:
            raise ValueError("You only have " + str(cart_quantity) + " " + item_name + " in cart")

        for i in range(quantity):
            cart.cart_items.remove(item_name)

        cart.store.items[item_name]["stock"] += quantity

        return item_name + " removed from cart"