items = {
    "Apple": 2,
    "Milk": 4,
    "Bread": 3,
    "Eggs": 5
}

cart = []

while True:
    print("\n1. Add Item to Cart")
    print("2. Display Cart")
    print("3. Calculate Total Cost")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Items:")
        for item, price in items.items():
            print(item, "-", price)

        item_name = input("Enter item name: ")

        if item_name in items:
            cart.append(item_name)
            print(item_name, "added to cart")
        else:
            print("Item not found")

    elif choice == 2:
        print("\nCart Items:")
        for item in cart:
            print(item)

    elif choice == 3:
        total_cost = 0

        for item in cart:
            total_cost = total_cost + items[item]

        print("Total Cost =", total_cost)

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")