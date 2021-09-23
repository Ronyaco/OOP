




class Person:
    def __init__(self, name, age, address, phone):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone

    def __str__(self):
        return self.__dict__.__str__()
    
    def greet(self):
        print("Hello I am ", self.name)

    def is_adult (self):
        if self.age >18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)