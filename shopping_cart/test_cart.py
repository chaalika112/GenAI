import unittest
from cart import Store, Cart, AddItem, DisplayCart, CalculateTotal, RemoveItem


class TestCart(unittest.TestCase):

    def setUp(self):
        print("\n========================================")
        print("Starting New Test")
        print("========================================")

        self.store = Store()
        self.cart = Cart(self.store)

        self.add = AddItem()
        self.display = DisplayCart()
        self.total = CalculateTotal()
        self.remove = RemoveItem()

    def tearDown(self):
        print("✓ Test Passed")

    def test_add_valid_item(self):
        print("Running: test_add_valid_item")
        print("Checking if Apple can be added to cart")

        message = self.add.add_item(self.cart, "Apple", 2)

        print("Cart:", self.cart.cart_items)

        self.assertIn("Apple", self.cart.cart_items)
        self.assertEqual(self.cart.cart_items.count("Apple"), 2)

    def test_add_invalid_item(self):
        print("Running: test_add_invalid_item")
        print("Checking if invalid item raises ValueError")

        with self.assertRaises(ValueError):
            self.add.add_item(self.cart, "Pizza", 1)

    def test_add_more_than_stock(self):
        print("Running: test_add_more_than_stock")
        print("Checking if quantity greater than stock raises ValueError")

        with self.assertRaises(ValueError):
            self.add.add_item(self.cart, "Apple", 10)

    def test_display_empty_cart(self):
        print("Running: test_display_empty_cart")
        print("Checking empty cart display")

        result = self.display.display_cart(self.cart)

        print("Output:", result)

        self.assertEqual(result, "\nCart is empty")

    def test_display_cart_with_items(self):
        print("Running: test_display_cart_with_items")
        print("Adding Apple x2 and displaying cart")

        self.add.add_item(self.cart, "Apple", 2)

        result = self.display.display_cart(self.cart)

        print("Output:", result)

        self.assertIn("Apple - 2", result)

    def test_calculate_total_empty_cart(self):
        print("Running: test_calculate_total_empty_cart")
        print("Checking total for empty cart")

        total = self.total.calculate_total(self.cart)

        print("Total:", total)

        self.assertEqual(total, 0)

    def test_calculate_total_with_items(self):
        print("Running: test_calculate_total_with_items")
        print("Adding Apple x2 and Milk x1")

        self.add.add_item(self.cart, "Apple", 2)
        self.add.add_item(self.cart, "Milk", 1)

        total = self.total.calculate_total(self.cart)

        print("Expected Total: 8")
        print("Actual Total:", total)

        self.assertEqual(total, 8)

    def test_remove_valid_quantity(self):
        print("Running: test_remove_valid_quantity")
        print("Adding Apple x5 then removing 2")

        self.add.add_item(self.cart, "Apple", 5)

        message = self.remove.remove_item(self.cart, "Apple", 2)

        print("Cart:", self.cart.cart_items)

        self.assertEqual(self.cart.cart_items.count("Apple"), 3)

    def test_remove_full_quantity(self):
        print("Running: test_remove_full_quantity")
        print("Adding Apple x2 then removing all")

        self.add.add_item(self.cart, "Apple", 2)

        self.remove.remove_item(self.cart, "Apple", 2)

        print("Cart:", self.cart.cart_items)

        self.assertNotIn("Apple", self.cart.cart_items)

    def test_remove_item_not_in_cart(self):
        print("Running: test_remove_item_not_in_cart")
        print("Checking if removing non-existing item raises ValueError")

        with self.assertRaises(ValueError):
            self.remove.remove_item(self.cart, "Eggs", 1)

    def test_remove_more_than_cart_quantity(self):
        print("Running: test_remove_more_than_cart_quantity")
        print("Adding Apple x2 and trying to remove 5")

        self.add.add_item(self.cart, "Apple", 2)

        with self.assertRaises(ValueError):
            self.remove.remove_item(self.cart, "Apple", 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)