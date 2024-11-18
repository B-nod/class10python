#encapsulation is the process of binding data and method in a single unit.

#data hiding in encapsulation
# Public - we can access the data from anywhere
# Protected - access the data within its class and its subclass
# Private - acces the data within only defined class

# class Person:
#     def __init__(self):
#         self.name = "Hari"  # Public
#         self.age = 25    # Protected
#         self.__address = "KTM" # Private

# person = Person()
# print(person.name)
# print(person._age)
# print(person._Person__address)

class Person:
    def __init__(self):
        self.name = "Hari"  
        self.age = 25    


class Office:
    def __init__(self):
        self._officeName = "Dursikshya"
        self._office_location ="Jamal"

    def office_detail(self):
        print("The office name is ", self._officeName, "The office location is ", self._office_location)

class Employee(Person, Office):
    def __init__(self, position, salary):
        self.__postion = position
        self.__salary = salary
        Person.__init__(self)
        Office.__init__(self)

    def show(self):
        print("Employee name : ", self.name, "\nEmployee age : ", self.age, "\nOffice name : ", self._officeName, "\nOffice location : ", self._office_location, "\nPosition : ", self.__postion, "\nSalary : ", self.__salary)

emp = Employee("Full stack developer", "Rs. 1000000")
emp.show()
    

