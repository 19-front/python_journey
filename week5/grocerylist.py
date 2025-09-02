class GroceryList:
    def __init__(self):
        self.items = {}
    def add_items(self, item, price):
        self.items[item] = price
    def show_items(self):
        return self.items
    def qty_list(self):
        return len(self.items)
    def total_cost(self):
        return sum(self.items.values())

my_list = GroceryList()
my_list.add_items("Milk", 16)
my_list.add_items("Sugar", 6)
my_list.add_items("Apple", 12)
my_list.add_items("Pasta", 8)
my_list.add_items("Water", 6)
print(my_list.show_items())
print("Items on Shoping Cart: ",my_list.qty_list())
print(f"Total Cost of Shopping: $",my_list.total_cost())