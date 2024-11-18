# is, is not => identity operator

x = 2
y = 2
print(id(x))
print(id(y))

x_list = [1,2,3]
y_list = [1,2,3]
print(id(x_list))
print(id(y_list))
print(x is y)
print( x_list is not y_list) 

# in , not in => membership operator
text = 'anfadksnfadsknfadsklnf'
print('z' in text)

z_list = ['football', 'volleyball', 'basketball']
email = ['binod@gmail.com', 'ram@gmail.com', 'manish@gmail.com']

print('volleyball' in z_list)
print('binod@gmail.com' not in email)
