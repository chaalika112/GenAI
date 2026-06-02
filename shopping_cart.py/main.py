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

            try:
                message = cart.add_item(item_name)
                print(message)

            except ValueError as e:
                print(e)

        elif choice == 2:
            print("\nCart Items:")

            result = cart.display_cart()

            if result == "Cart is empty":
                print(result)
            else:
                for item in result:
                    print(item)

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