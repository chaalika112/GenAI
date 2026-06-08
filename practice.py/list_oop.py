class Cart:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

c1 = Cart()

c1.add_item("Apple")
c1.add_item("Milk")

print(c1.items)

