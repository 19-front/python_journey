class Queue:
    def __init__(self):
        self.items = []
    

    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
    
    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print(f"\n{flavor}, not available\n")
            return
        if scoops < 1 or scoops > 3:
            print("\nChoose number of Scoop 1 - 3\n")
            return
        
        print("Order created")
        order = {
            "customer": customer,
            "flavor": flavor,
            "scoops": scoops
            }
        self.orders.enqueue(order)
        

    def show_all_orders(self):
        if self.orders.size() == 0:
            print("\nNo pending orders.\n")
        else:
            print("\nAll pending orders here: ")
        for order in self.orders.items:
                print(
                    f"Customer: {order['customer']} "
                    f"Flavor: {order['flavor']} "
                    f"Scoops: {order['scoops']}"
                )
    

    def next_order(self):
        order = self.orders.dequeue()
        if order:
            print("\nNext Order Up:")
            print(f"Customer: {order['customer']}, Flavor: {order['flavor']}, Scoops: {order['scoops']}")
        else:
            print("\nNo pending orders")

  

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])

shop.take_order("Zachary", "pistachia", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
