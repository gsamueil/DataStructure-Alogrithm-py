"""How to check if an array contain a number in python"""
import numpy as np
my_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def find_element(array, number):
    for i in range(len(my_array)):
        if array[i]== number:
            print(i)

find_element(my_array,11)