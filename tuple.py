#tuple is used to stoer multiple values which is structure, allow duplicate value and immutable. It is denoted by ()

p_language = ('PHP', 'Python', 'Javascript', 'Python', 'Python', 1)
print(p_language)
print(type(p_language))
print(len(p_language))

print(p_language.index('Javascript'))
print(p_language.count("Python")) 

list_language = list(p_language)
print(type(list_language))