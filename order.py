class Order:
    def __init__(self):
        self.cart_items=[]  

    def add_item(self,ordered_item):
        for item in self.cart_items:
            if item.name==ordered_item.name:
                item.quantity+=ordered_item.quantity
                break
        else:               #this is a for...else loop, here if break does not excute then only else excute
            self.cart_items.append(ordered_item)

            

    def remove(self,item):
        if item in self.cart_items:
            del self.cart_items[item]

    def total_price(self):
        return sum(item.price * item.quantity for item in self.cart_items)
     
    def clear(self):
        self.cart_items=[]