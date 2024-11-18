#polymorphism means having different form

class Vehicle:
    def grea(self):
        print("Every vehicle have grea system")

    def max_speed(self):
        print("Every vehilce have their own max speed")

class Car(Vehicle):
    def grea(self):
        print("Car have 5 grea system")

    def max_speed(self):
        print("Car have max speed 200 km/hr")

class Bike(Vehicle):
    def grea(self):
        print("Bike have have 5 grea system")

    def max_speed(self):
        print("Bike have max speed 150 km/hr ")

car = Car()
car.grea()
car.max_speed()

bike = Bike()
bike.grea()
bike.max_speed()


#another example
import math

class Shape:
    def area(self):
        return NotImplementedError("Its sub-class is not implement the parent method")
    
class Sqaure(Shape):
    def area(self, length):
        self.length = length
        return self.length*self.length
    
class Circle(Shape):
    def area(self, radius):
        self.radius = radius
        return math.pi * self.radius*self.radius 
         
    def show(self):
        print("Circle")
    
square = Sqaure()
print(square.area(5))
circle = Circle()
circle.show()
print(circle.area(4))