from cart import Store, Cart, AddItem, DisplayCart, CalculateTotal, RemoveItem, User


store = Store()
user = User(store)

add = AddItem()
display = DisplayCart()
total_cost = CalculateTotal()
remove = RemoveItem()


while True:
    print("\n1. Sign Up")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")

        store.cursor.execute(
           "SELECT * FROM Users WHERE username = ?",
           (username,)
        )

        if store.cursor.fetchone() is not None:
            print("Username already exists")
            continue

        password = input("Enter password: ")

        try:
            message = user.signup(username, password)
            print(message)
            print("Please login to continue.")
        except ValueError as e:
            print(e)

    elif choice == 2:
        username = input("Enter username: ")

        store.cursor.execute(
           "SELECT * FROM Users WHERE username = ?",
           (username,)
        )

        result = store.cursor.fetchone()

        if result is None:
            print("Username does not exist")
            continue

        password = input("Enter password: ")

        try:
            user_id = user.login(username, password)
            print("Login successful")

            cart = Cart(store, user_id)

            while True:
                print("\n1. Add Item to Cart")
                print("2. Display Cart")
                print("3. Calculate Total Cost")
                print("4. Remove Items")
                print("5. Delete Account")
                print("6. Logout")

                try:
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        store.display_items()

                        item_name = input("Enter item name: ")
                        quantity = int(input("Enter quantity: "))

                        try:
                            message = add.add_item(cart, item_name, quantity)
                            print(message)
                        except ValueError as e:
                            print(e)

                    elif choice == 2:
                        result = display.display_cart(cart)

                        if result == "\nCart is empty":
                            print(result)
                        else:
                            print("\nCart Items:")
                            for item in result:
                                print(item)

                    elif choice == 3:
                        total = total_cost.calculate_total(cart)
                        print("Total Cost =", total)

                    elif choice == 4:
                        result = display.display_cart(cart)

                        if result == "\nCart is empty":
                            print(result)
                        else:
                            print("\nCart Items:")
                            for item in result:
                                print(item)

                            while True:
                                try:
                                    remove_item = input("\nEnter item name to remove: ")

                                    store.cursor.execute(
                                        "SELECT quantity FROM Cart WHERE item_name = ? AND user_id = ?",
                                        (remove_item, cart.user_id)
                                    )

                                    if store.cursor.fetchone() is None:
                                        print("Item not found in cart")
                                        continue

                                    remove_quantity = int(input("Enter quantity to remove: "))

                                    message = remove.remove_item(cart, remove_item, remove_quantity)
                                    print(message)

                                    print("\nUpdated Cart Items:")

                                    result = display.display_cart(cart)

                                    if result == "\nCart is empty":
                                        print(result)
                                    else:
                                        for item in result:
                                            print(item)

                                    break

                                except ValueError as e:
                                    print(e)
                    elif choice == 5:
                       confirm = input("Are you sure you want to delete your account? (yes/no): ")

                       if confirm.lower() == "yes":

                          store.cursor.execute(
                               "DELETE FROM Cart WHERE user_id = ?",
                               (cart.user_id,)
                          )

                          store.cursor.execute(
                               "DELETE FROM Users WHERE Id = ?",
                               (cart.user_id,)
                          )

                          store.conn.commit()

                          print("Account deleted successfully")
                          break

                       else:
                          print("Account deletion cancelled")
                          
                    elif choice == 6:
                        print("Logged out")
                        break

                    else:
                        print("Invalid Choice")

                except ValueError:
                    print("Please enter a valid number.")

        except ValueError as e:
            print(e)

    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")