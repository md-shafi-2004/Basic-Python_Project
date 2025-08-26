from food_item import Fooditem
from menu import Menu
from order import Order
from restaurant import Restaurant
from user import Customer,Admin,Employee

dominoes=Restaurant("Dominoes")
def customer_menu():
    name=input("Enter your name : ")
    email=input("Enter your email : ")
    phone=input("Enter your phone : ")
    address=input("Enter your address : ")
    customer=Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name} !!")
        print("1. View menu")
        print("2. Add item to cart")
        print("3. View cart") 
        print("4. Pay bill")
        print("5. Exit")

        choice=int(input("Enter your choice : "))
        if choice==1:
            customer.view_menu(dominoes)
        elif choice==2:
            item_name=input("Enter item name : ")
            item_quantity=int(input("Enter item quantity : "))
            customer.add_to_cart(dominoes,item_name,item_quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid Choice !!")
        

def admin_menu():
    name=input("Enter your name : ")
    email=input("Enter your email : ")
    phone=input("Enter your phone : ")
    address=input("Enter your address : ")
    admin=Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name} !!")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee") 
        print("4. View items")
        print("5. Delete item")
        print("6. Exit")

        choice=int(input("Enter your choice : "))
        if choice==1:
            item_name=input("Enter item name : ")
            item_price=int(input("Enter item price : "))
            item_quantity=int(input("Enter item quantity : "))
            item=Fooditem(name=item_name,price=item_price,quantity=item_quantity)
            admin.add_new_item(dominoes,item)
        elif choice==2:
            name=input("Enter employee name : ")
            email=input("Enter employee email : ")
            phone=input("Enter employee phone : ")
            address=input("Enter employee address : ")
            age=input("Enter employee age : ")
            designation=input("Enter employee designation : ")
            salary=input("Enter employee salary : ")
            employee=Employee(name,email,phone,address,age,designation,salary)
            admin.add_employee(dominoes,employee)
        elif choice==3:
            admin.view_employee(dominoes)
        elif choice==4:
            admin.view_items(dominoes)
        elif choice==5:
            item_name=input("Enter item name : ")
            admin.remove_item(dominoes,item_name)
        elif choice==6:
            break
        else:
            print("Invalid Choice !!")


while True:
    print("Welcome!!")
    print("1. Customer : ")
    print("2 . Admin : ")
    print("3 . Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid input!!")

