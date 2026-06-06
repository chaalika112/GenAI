import unittest
from cart import Store, Cart


class TestCart(unittest.TestCase):

    def test_add_item(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        self.assertIn("Apple", cart.cart_items)
        self.assertEqual(cart.cart_items["Apple"], 2)

    def test_add_same_item_again(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)
        cart.add_item("Apple", 3)

        self.assertEqual(cart.cart_items["Apple"], 5)

    def test_invalid_item(self):
        store = Store()
        cart = Cart(store)

        with self.assertRaises(ValueError):
            cart.add_item("Pizza", 1)

    def test_add_zero_quantity(self):
        store = Store()
        cart = Cart(store)

        with self.assertRaises(ValueError):
            cart.add_item("Apple", 0)

    def test_add_negative_quantity(self):
        store = Store()
        cart = Cart(store)

        with self.assertRaises(ValueError):
            cart.add_item("Apple", -2)

    def test_display_empty_cart(self):
        store = Store()
        cart = Cart(store)

        self.assertEqual(cart.display_cart(), "\nCart is empty")

    def test_display_cart_with_items(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        result = cart.display_cart()

        self.assertIn("Apple", result[0])

    def test_total_cost(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 1)
        cart.add_item("Milk", 1)

        self.assertEqual(cart.calculate_total(), 6)

    def test_total_cost_empty_cart(self):
        store = Store()
        cart = Cart(store)

        self.assertEqual(cart.calculate_total(), 0)

    def test_remove_item(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 3)
        cart.remove_item("Apple", 1)

        self.assertEqual(cart.cart_items["Apple"], 2)

    def test_remove_full_quantity(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)
        cart.remove_item("Apple", 2)

        self.assertNotIn("Apple", cart.cart_items)

    def test_remove_invalid_item(self):
        store = Store()
        cart = Cart(store)

        with self.assertRaises(ValueError):
            cart.remove_item("Pizza", 1)

    def test_remove_more_than_available(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        with self.assertRaises(ValueError):
            cart.remove_item("Apple", 5)

    def test_remove_zero_quantity(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        with self.assertRaises(ValueError):
            cart.remove_item("Apple", 0)

    def test_remove_negative_quantity(self):
        store = Store()
        cart = Cart(store)

        cart.add_item("Apple", 2)

        with self.assertRaises(ValueError):
            cart.remove_item("Apple", -1)


if __name__ == "__main__":
    unittest.main()