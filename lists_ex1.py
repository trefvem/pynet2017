my_list = ['name', 'next', 'more', 'continued', 'last']
print(my_list)
my_list.append('new')
my_list.append('another')
print(my_list)
print(my_list.pop(0))

print("Length of list: {}".format(len(my_list)))
my_list.sort()
print(my_list)
id(my_list)
new_list = my_list[:]
print new_list
id(new_list)
