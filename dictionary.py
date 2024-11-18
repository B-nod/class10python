#dictionary is used to store multiple values in key:value pairs

capital = {'Nepal':'Kathmandu', 'India':'New Delhi'}
print(capital)
print(type(capital))
print(len(capital))
capital['Japan'] = 'Tokyo'  # to add data in dictionary
print(capital)

print(capital.keys())
print(capital.values())
print(capital.items())
capital.clear()
print(capital)