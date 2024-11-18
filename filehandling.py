path = 'demo.txt'

# new_file = open(path)
# print(new_file)
# print(new_file.readable())
# print(new_file.writable())
# print(new_file.read())
# new_file.close()

# another_file = open(path, 'r+')
# print(another_file)
# print(another_file.readable())
# print(another_file.writable())
# print(another_file.read())
# another_file.write('\n Another studnet name is Ram ')
# print(another_file.seek(0))
# print(another_file.read())
# another_file.close()

# w_file = open(path, 'w+')
# print(w_file)
# print(w_file.readable())
# print(w_file.writable())
# w_file.write('New student name is Shyam \n')
# w_file.seek(0)
# print(w_file.read())
# w_file.close()

import shutil,os
# shutil.copy('demo.txt', 'c_demo.txt')
# shutil.move('c_demo.txt', 'hello.txt')
os.remove('hello.txt')

# a+ mode
