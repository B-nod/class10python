# inheritance is the way of transforming the characteristic of parent class to its child class. advantage of inheritance is for reusable of code for software development.

# four types of inheritance
#single inheritance
#Mutliple   inheritance
#hierarchical inheritance
#Multilevel inheritance

#single level inheritance

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
         print("Show the student detail")

class Course:
    def __init__(self, course):
        self.course = course

#Multiple Inheritance
class College(Student, Course):
    def __init__(self,name, age, college_name):
        Student.__init__(self,name,age)
        self.college_name = college_name

        print("The student name is ", self.name, "The college name is ", self.college_name)
    
    def show(self):
        Student.show(self)
        print("Show the college detail")


college = College('binod', 20, 'ismt')
college.show()

#MultiLevel Inheritance
class StudentDetail(College):
    def detail(self):
        super().show()
        print("Another child class.")

detail = StudentDetail('Ram', 16, "Xavier")
detail.detail()

