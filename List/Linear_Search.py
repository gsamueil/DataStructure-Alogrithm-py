"""Searching for an element in the list"""

my_list = [10,20,30,40,50,60,70,80,90]

def search_list(list,  value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(search_list(my_list, 80))