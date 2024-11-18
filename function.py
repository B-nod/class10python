# function is a block of code which can be reuse again and again.

#defining function
# def demoFunction():
#     print("Welcome to our python class")


# #call the function
# demoFunction()

# def area(a, b): #parameter
#     print("The area of given object is ", a*b)

# area(10,15) #arguments
# area(20,24)

#positional arguments

# def student(name, subject):
#     print("student name is ", name, "student chossen subject is ", subject)

# student('Ayush','Full stack')
# student('Data science', 'Ram')

#keyword arguments
# student(subject='Data Scince', name='Ram')

# student('Hari', 'Python', 'HTML')

#*args -> arbitary arguments where we can pass unlimited value
    
# def student(*args):
#     print("student name is ", args[0], "student chossen subject is ", args[1])

# student('Hari', 'Python', 'HTML', 'css', 'react')

# def number(*args):
#     total = 0
#     for i in args:
#         total+=i

#     return f"Total= {total}" # return type stop the exceution of function and gives the final output
    

# print(number(1,2,3,4,5,6,7))


#**kwargs => keyword arbitary arguments which can pass unlimited data in key:value pair

# def student(**kwargs):
#     print("student name is ", kwargs['name'], "student chossen subject is ", kwargs['course4'])

# student(name='Hari', course1='Python', couse2='HTML', course3='css', course4='react')

#scope of varaible
# global variable and local varible

# l = int(input("Enter a length : ")) #global variable which can be access through any where
# w = int(input("Enter a wdith : "))

# def area():
#     global h # to convert local variable into global 
#     h = int(input("Enter a height"))  #local variable which can be access only inside the define class

#     return f"area of object = {l*w} Height = {h}"

# def volume():
#     return f"volume of object = {l*w*h}"

# print(area())
# print(volume())


#lambda function- the function which is create for instance use by using lambda keyword

x = lambda a,b:a+b

print("The addition of two number is ",x(2,5))


#recursive function -> the function which is called by itself 

def factorial(num):
    if num ==0:
        return 1
    else:
        return num*factorial(num-1)
    
fact = factorial(int(input("Enter a number for factorial = ")))
print("The factorail of given number is ", fact)

#map
#filter
#reduce