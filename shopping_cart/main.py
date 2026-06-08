from cart import Store, Cart

store = Store()
cart = Cart(store)

while True:
    print("\n1. Add Item to Cart")
    print("2. Display Cart")
    print("3. Calculate Total Cost")
    print("4. Remove Items")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            store.display_items()

            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))

            try:
                message = cart.add_item(item_name, quantity)
                print(message)
            except ValueError as e:
                print(e)

        elif choice == 2:
            result = cart.display_cart()

            if result == "\nCart is empty":
                print(result)
            else:
                print("\nCart Items:")
                for item in result:
                    print(item)

        elif choice == 3:
            total = cart.calculate_total()
            print("Total Cost =", total)

        elif choice == 4:
            result = cart.display_cart()

            if result == "\nCart is empty":
               print(result)
            else:
               print("\nCart Items:")
               for item in result:
                   print(item)

               while True:
                   try:
                      remove_item = input("\nEnter item name to remove: ")

                      if remove_item not in cart.cart_items:
                         print("Item not found in cart")
                         continue

                      remove_quantity = int(input("Enter quantity to remove: "))

                      message = cart.remove_item(remove_item, remove_quantity)
                      print(message)

                      print("\nUpdated Cart Items:")

                      result = cart.display_cart()

                      if result == "\nCart is empty":
                         print(result)
                      else:
                         for item in result:
                             print(item)

                      break

                   except ValueError as e:
                        print(e)
        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter a valid number.")