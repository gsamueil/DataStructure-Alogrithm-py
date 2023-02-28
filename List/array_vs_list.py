"""Array vs list"""
from random import shuffle
import random
import numpy as np
my_array = np.array([1,2,3,4,5,6])
my_list = [1,2,3,4,5,6]
# print(my_array/2) # it will give right result
# print(my_list/2)# it will give error  because this integer number on list 


# n_my_array = np.array([1,2,3,4,5,6,'a'])
# n_my_list = [1,2,3,4,5,6, 'a']
# print(n_my_array) # it will give right result
# print(n_my_list)#
"""Exam  9 examples"""
#lst[initial : End : IndexJump]
# a= [1,2,3,4,5]
# # -1 mean jump step and start with index 3 (value [4]) and go to index 0 
# print(a[3:0:-1])#[4, 3,  2]
#################################################################
# fruit = ['Apple', 'Banana', 'Papaya', 'Cherry']
# random.shuffle(fruit)
# print(fruit)
#################################################################
# def f(value, values):
#     v =1
#     values[0] = 44
# t=3
# v = [1,2,3]
# f(t,v)#this function accept t=3 it will override the value inside the function but the another argument with still as 44 because this is list 
# print(t, v[0])

#################################################################
# arr = [1,2,3,4,5,6]
# for i in range(1, 6):# i = 2,3,4,5,6
#     arr[i-1] = arr[i]  #1-1=0  2-1=1 3-1=2 4-1=3  5-1=4   (2,3,4,5,6,6)
#     print(arr[i])   
# for i in range(0, 6):
#     print(arr[i], end = " ")
###################################################################
# a= [1,2,3,4,5,6,7,8,9]
# print(a[::2])
#####################################################################
# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10,20,30,40,50,60
# print(a)
######################################################################
# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print(data[0])
# def fun(m):
#     v = m[0][0]
#     #print(v)
#     for row in m:
#         #print(row)
#         for element in row:
#             print(element)
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))
########################################################################

 
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
 
# print(sum)
########################################################################

# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())

