#Lab Assignment-1

"""
Create a class Employee inherits it into another class Manager Add methods to get input & print 
information of employees. Consider the attributes name, age, salary, address etc. process the 
information of 10 managers

"""

class Employee:
    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

class Manager(Employee):
    def display(self):
        print("\nManager Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


managers = []

for i in range(10):
    print("\nEnter details of Manager", i+1)
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n----- Manager Details -----")
for m in managers:
    m.display()