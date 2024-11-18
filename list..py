# list is used to store multiple value which is ordered, changeable and allow duplicate. it is denoted by square bracket []
laptops = ['Dell', 'Mac', 'Hp', 'Lenevo']
print(len(laptops)) # to know length of list
print(type(laptops)) # to know the types

# to access the value through index
print(laptops[0])

#index()-> to know the index number of given element
print(laptops.index('Lenevo'))

#append()-> to add the element from the last index of the list
laptops.append('Acer')
print(laptops)

#insert()-> to add the element in mentioned index 
laptops.insert(3,'Dell')
print(laptops)

#count()-> to count the element in the list
print(laptops.count('Mac'))

#pop() ->to remove the element from the last index of the list as well as return the removed element or remove element from mentioned index
pop_element = laptops.pop(2)
print(pop_element)
print(laptops)

#extend()
p_language = ['HTML', 'CSS', 'PHP']
laptops.extend(p_language)
print(laptops)

laptops.reverse()
print(laptops)

#sort() -> ascending order 
laptops.sort(reverse=True)
print(laptops)

#reverse() 
laptops.reverse()
print(laptops)

#remove()
laptops.remove('CSS')
print(laptops)
