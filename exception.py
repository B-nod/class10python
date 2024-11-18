#exception handling -> to maintain the normal flow of the code
# try:
#     a = int(input("Enter a number = "))
#     b = int(input("Enter a second number = "))
#     c = a+b
 
# except:
#     print("The value must be integer")
# else:
#     print("The addition of two number is ", c)
#     print("Succesfully done")


# print("Welcome to dursikshya")

# try:
#     a = int(input("Enter a first number = "))
#     b = int(input("Enter a second number = "))
#     c = a/b
# except ValueError:
#     print("The value must be integer")
# except ZeroDivisionError:
#     print("Zero cannot divide other number")

# else:
#     print("The division of two number is ", c)

#raise 
def login():
    try:
        username = 'binod'
        pin = 1234
        r_username = input("Enter your username = ")
        r_pin = int(input("Enter your pin = "))
        if username != r_username:
            raise IndentationError
        if pin != r_pin:
            raise ZeroDivisionError
    except IndentationError:
        print("Username is invalid")
        login()
    except ZeroDivisionError:
        print("Password is invalid")
        login()
    else:
        print("Welcome to User dashboard")
    finally:
        print("hello")

    print("Welcome")



login()

