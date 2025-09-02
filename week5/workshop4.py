class GroceryList:
    def __init__(self):
        self.items = []
    def add_items(self, item):
        self.items.append(item)
    def remove_items(self, item):
        self.items.remove(item)
    def show_items(self):
        return self.items
    def total_items(self):
        return len(self.items)

my_List = GroceryList()
my_List.add_items("milk")
my_List.add_items("tea")
my_List.add_items("bowls")
print(my_List.show_items())
my_List.add_items("pencils")
my_List.add_items("books")
print(my_List.show_items())
print(my_List.total_items())
my_List.remove_items("milk")
my_List.remove_items("pencils")
print(my_List.show_items())
print(my_List.total_items())