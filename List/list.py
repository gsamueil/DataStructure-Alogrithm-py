# course = ['history','Math','Physics','ComSci','Science']
# print(len(course))
# print(course[0])
# print(course[3:])# first index is our starting point and the second index stop point and if we neen to include all index we will not put the stop point
# course.append('morophology')
# course.insert(1,"arabic")
# print(course[-1])
# print(course)

# #insert list inside list
list_1=['history','Math','Physics','ComSci','Science']
list_2=['a','b']
#list_1.insert(0,list_2)
#print(list_1)
# list_1.extend(list_2)
# print(list_1)
# pooped = list_1.pop()
# print(pooped)
# print(list_1)
# list_1.reverse()
# print(list_1)
# list_1.sort()
# print(list_1)
# list_1.sort(reverse=True)
# print(list_1)
# for item in list_1:
#     print(item)

# for index, course in enumerate(list_1):
#     print(index, course)
list_str = ' - '.join(list_1)
new_list= list_str.split(' - ')
print(list_str)
print(new_list)