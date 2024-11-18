# loop denotes repetation or iteration
sports = ['football', 'volleyball', 'basketball']
for i in sports:
    print(i)

#range()
for i in range(1, 11):
    print(i)

x = int(input('Enter a number : '))
for i in range(1,11):
    print(i , "X", x, "=", i*x)

#sum of list
number = [1,2,3,4,5]
total = 0
for i in number:
    total+=i
print(total)