import sqlite3
from datetime import datetime

class Store:
    def __init__(self):
        self.conn = sqlite3.connect("shopping_cart.db")
        self.cursor = self.conn.cursor()

    def display_items(self):
        self.cursor.execute("SELECT * FROM Items")
        rows = self.cursor.fetchall()

        print("\nAvailable Items:")
        for row in rows:
            print(row[1], "- Price:", row[2], "- Stock:", row[3])

    def check_item(self, item_name):
        self.cursor.execute(
            "SELECT Stock FROM Items WHERE item_name = ?",
            (item_name,)
        )

        result = self.cursor.fetchone()

        if result is None:
            raise ValueError("Item not found")

        stock = result[0]

        if stock <= 0:
            raise ValueError("Item is out of stock")

        return stock

    def get_price(self, item_name):
        self.cursor.execute(
            "SELECT Price FROM Items WHERE item_name = ?",
            (item_name,)
        )

        result = self.cursor.fetchone()
        return result[0]

    def reduce_stock(self, item_name, quantity):
        self.cursor.execute(
            "UPDATE Items SET Stock = Stock - ? WHERE item_name = ?",
            (quantity, item_name)
        )
        self.conn.commit()

    def increase_stock(self, item_name, quantity):
        self.cursor.execute(
            "UPDATE Items SET Stock = Stock + ? WHERE item_name = ?",
            (quantity, item_name)
        )
        self.conn.commit()


class User:
    def __init__(self, store):
        self.store = store

    def signup(self, username, password):
        self.store.cursor.execute(
            "SELECT * FROM Users WHERE username = ?",
            (username,)
        )

        result = self.store.cursor.fetchone()

        if result is not None:
            raise ValueError("Username already exists")

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.store.cursor.execute(
            "INSERT INTO Users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, created_at)
        )

        self.store.conn.commit()
        return "Signup successful"

    def login(self, username, password):
        self.store.cursor.execute(
            "SELECT Id FROM Users WHERE username = ? AND password = ?",
            (username, password)
        )

        result = self.store.cursor.fetchone()

        if result is None:
            raise ValueError("Invalid username or password")

        return result[0]


class Cart:
    def __init__(self, store, user_id):
        self.store = store
        self.user_id = user_id


class AddItem:
    def add_item(self, cart, item_name, quantity):
        stock = cart.store.check_item(item_name)

        if quantity > stock:
            raise ValueError("Only " + str(stock) + " items available")

        price = cart.store.get_price(item_name)

        cart.store.cursor.execute(
            "SELECT quantity FROM Cart WHERE item_name = ? AND user_id = ?",
            (item_name, cart.user_id)
        )

        result = cart.store.cursor.fetchone()

        if result is None:
            cart.store.cursor.execute(
                "INSERT INTO Cart (item_name, quantity, Price, user_id) VALUES (?, ?, ?, ?)",
                (item_name, quantity, price, cart.user_id)
            )
        else:
            cart.store.cursor.execute(
                "UPDATE Cart SET quantity = quantity + ? WHERE item_name = ? AND user_id = ?",
                (quantity, item_name, cart.user_id)
            )

        cart.store.reduce_stock(item_name, quantity)
        cart.store.conn.commit()

        return item_name + " added to cart"


class DisplayCart:
    def display_cart(self, cart):
        cart.store.cursor.execute(
            "SELECT item_name, quantity FROM Cart WHERE user_id = ?",
            (cart.user_id,)
        )

        rows = cart.store.cursor.fetchall()

        if len(rows) == 0:
            return "\nCart is empty"

        result = []

        for row in rows:
            result.append(row[0] + " - " + str(row[1]))

        return result


class CalculateTotal:
    def calculate_total(self, cart):
        cart.store.cursor.execute(
            "SELECT quantity, Price FROM Cart WHERE user_id = ?",
            (cart.user_id,)
        )

        rows = cart.store.cursor.fetchall()

        total_cost = 0

        for row in rows:
            total_cost += row[0] * row[1]

        return total_cost


class RemoveItem:
    def remove_item(self, cart, item_name, quantity):
        cart.store.cursor.execute(
            "SELECT quantity FROM Cart WHERE item_name = ? AND user_id = ?",
            (item_name, cart.user_id)
        )

        result = cart.store.cursor.fetchone()

        if result is None:
            raise ValueError("Item not found in cart")

        cart_quantity = result[0]

        if quantity > cart_quantity:
            raise ValueError("You only have " + str(cart_quantity) + " " + item_name + " in cart")

        if quantity == cart_quantity:
            cart.store.cursor.execute(
                "DELETE FROM Cart WHERE item_name = ? AND user_id = ?",
                (item_name, cart.user_id)
            )
        else:
            cart.store.cursor.execute(
                "UPDATE Cart SET quantity = quantity - ? WHERE item_name = ? AND user_id = ?",
                (quantity, item_name, cart.user_id)
            )

        cart.store.increase_stock(item_name, quantity)
        cart.store.conn.commit()

        return item_name + " removed from cart"