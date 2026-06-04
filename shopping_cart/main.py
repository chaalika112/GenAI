from cart import Store, Cart

store = Store()
cart = Cart(store)

while True:
    print("\n1. Add Item to Cart")
    print("2. Display Cart")
    print("3. Calculate Total Cost")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            store.display_items()

            item_name = input("Enter iten name: ")
            quantity = int(input("Enter quantity: "))

            try:
                message = cart.add_item(item_name, quantity)
                print(message)

            except ValueError as e:
                print(e)

        elif choice == 2:

            cart.display_cart()

            remove_item = input(
             "\nEnter item name to remove (or press Enter): "
            )

            if remove_item != "":
              cart.remove_item(remove_item)
              print("Item removed successfully")

        elif choice == 3:
              total = cart.calculate_total()
              print("Total Cost =", total)

        elif choice == 4:
              print("Thank You!")
              break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number.")