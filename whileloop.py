x = 1
while(x<11):
    if x == 5:
        break
    print(x)
    x+=1

for i in range(1, 10):
    if i%2==0:
        continue
    print(i)

color = ['white', 'black', 'red', 'yellow']
sports = ['football', 'volleyball', 'basketball', 'hockey']
#outer loop
for i in color:
    #inner loop
    for j in sports:
        print(i,j)


#for inside while => multiplication table

# to check even number => if user gives odd number continue the loop and again ask user to put the input. If user gives even number and break the loops and give message Thank you. You have enter the even number.