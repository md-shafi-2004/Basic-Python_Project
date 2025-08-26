from abc import ABC
from order import Order 
from food_item import Fooditem
from menu import Menu

class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart=Order()

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,ordered_quantity):
        inventory_item=restaurant.menu.find_item(item_name)
        if inventory_item:
            if ordered_quantity>inventory_item.quantity:
                print("Item quantity exceeded !!")
            else:
                ordered_item=Fooditem(item_name,inventory_item.price,ordered_quantity)
                self.cart.add_item(ordered_item)
                print("Item added")
        else:
            print("item not found")

    def view_cart(self):
        print("*******View Cart*******")
        print("Name\tPrice\tQuantity")
        for item in self.cart.cart_items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")
        print(f"To proceed to the payment enter your total amount in Pay Bill option\nPayable amount is : {self.cart.total_price()}")

    def pay_bill(self,restaurant,total_amount):  #only when customer will pay successfully then stock will reduce from menu database
        if total_amount==self.cart.total_price():
            print(f"Total {total_amount} paid successfully")
            for item in self.cart.cart_items:
                inventory_item=restaurant.menu.find_item(item.name)
                inventory_item.quantity-=item.quantity
            self.cart.clear()
        else:
            if total_amount>self.cart.total_price():
                print(f"You have entered {total_amount-self.cart.total_price()} more!!")
                self.view_cart()
            else:
                print(f"You have entered {self.cart.total_price()-total_amount} less!!")
                self.view_cart()

class Employee(User):
    def __init__(self, name, email, phone, address,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, email, phone, address)

class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
    
    def view_items(self,restaurant):
        restaurant.menu.show_menu()
    
    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)



    






