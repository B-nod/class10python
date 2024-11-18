# set is used to store multiple values which contain only unique element, data are store in unstructure way and it is changeable. it is denoted by {}

unique_id = {101, 102, 103, 101, 102, 'python'}
print(unique_id)

p_language = ('PHP', 'Python', 'Javascript', 'Python', 'Python', 1)

unique_language = set(p_language)
print(unique_language)
unique_language.add('Java')  # to add the value in set
print(unique_language)

unique_language.update(unique_id) # to concat the two set
print(unique_language)

unique_language.remove('Java') # to remove the specific data from the set
print(unique_language)

pop_element = unique_language.pop() # to remove the random data from the set
print(pop_element)
print(unique_language)

copy_set = unique_language.copy() # to copy the set
print(copy_set)

copy_set.clear() # to clear all data from the set
print(copy_set)

sports = []  # define empty list
empty_set = set()
empty_set.add('Ram')
print(empty_set)

dictionry = {}