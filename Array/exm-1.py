""" Array is a data structure consisting of a collection of elements , each identified by at least one array index or key .
    An array is stored such that the position of each element can be computed from its index by a mathematical formula.
"""
#types of ARRAY ------> ONE Dimensional and Two Dimensional

from array import *

arr1 = array('i' , [1,3,3,4,7])
print(arr1)
#how to insert to array
arr1.insert(0,9)
print(arr1)
"""traverse array"""
def traverse_array(array):
    for i in array:
        print(i)
    
traverse_array(arr1)

"""access elements"""
def access_element(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

print('the index you need is ' )
access_element(arr1, 4)