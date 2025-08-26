from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]  #this is our database
        self.menu=Menu()

    def add_employee(self,employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee list !!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address,emp.age,emp.designation,emp.salary)

    def view_menu(self):
        self.menu.show_menu()