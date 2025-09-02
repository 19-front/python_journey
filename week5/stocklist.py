class StockList:
    def __init__(self):
        self.items = []
    def add_stock(self, item):
        self.items.append(item)
    def remove_stock(self, item):
        self.items.remove(item)
    def show_stock(self):
        return self.items
    def total_stock(self):
        return len(self.items)

my_stock = StockList()
my_stock.add_stock("Nail")
my_stock.add_stock("Hammer")
my_stock.add_stock("Plywood")
print(my_stock.show_stock())
print(my_stock.total_stock())
my_stock.add_stock("Wire mesh")
my_stock.add_stock("Cement")
my_stock.remove_stock("Nail")
print(my_stock.show_stock())
print(my_stock.total_stock())
