import unittest
from cart import Store, Cart


class TestCart(unittest.TestCase):

    def test_add_item(self):
        print("Running test_add_item")

        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        self.assertIn("Apple", cart.cart_items)

    def test_invalid_item(self):
        print("Running Test to check invalid item error")

        store = Store()
        cart = Cart(store)

        with self.assertRaises(ValueError):
            cart.add_item("Pizza", 1)

    def test_total_cost(self):
        print("Running to check total cost")

        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 1)
        cart.add_item("Milk", 1)

        self.assertEqual(cart.calculate_total(), 6)


if __name__ == "__main__":
    unittest.main()