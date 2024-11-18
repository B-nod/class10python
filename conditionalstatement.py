# if else, if elif , nesting if

# age = int(input("Enter a age : "))
# if age >= 18 and age <=59:
#     print("You are eligible for citizenship")
# elif age >=60:
#     print("Senior Citizenship")
# else:
#     print("You are not eligible ")

#atm machine 15 min
def atm():
    pin = 1234
    user_pin = int(input("Enter a pin : "))
    if user_pin == pin:
        choose_num = int(input("Choose an option: \n1. Fast Cash \n2. Withdraw \n3. Balance Inquery \n4. Cancel\nEnter a number : "))
        if choose_num == 1:
            fast_num = int(input("Choose an option: \n1. 1000 \n2. 2000 \n3. 5000 \n4. 10000\nEnter a number : "))
            if fast_num == 1:
                print("You have withdrawn Rs. 1000")
            elif fast_num == 2:
                print("You have withdrawn Rs. 2000")
            elif fast_num == 3:
                print("You have withdrawn Rs. 5000")
            elif fast_num == 4:
                print("You have withdrawn Rs. 10000")
            else:
                print("You choose wrong option")
        elif choose_num == 2 :
            withdraw = int(input("Enter an amount : "))
            print("You have withdrawn Rs.", withdraw)
        elif choose_num == 3:
            print("You account balance is Rs. 200000")
        elif choose_num == 4:
            print('You are successfully logout')
        else:
            print("You choose wrong option")
    else:
        print('Wrong pin')
        atm()

atm()