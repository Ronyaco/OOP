
from Person import Person

class Employee(Person):
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        """self.name = name
        self.age = age
        self.address = address
        self.phone = phone"""
        """Person.__init__(self, name, age, address, phone)"""
        super.__init__(self, name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone


    def calculate(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    def contact_details(self):
        """Person.contact_details(self)"""
        super().contact_details()
        print(self.office_address, self.office_phone)