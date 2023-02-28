""" List operations /functions """
"""
+ operator : concatenate Lists
list1=[1,2]
list2=[1.3]
list1+list2=[1,2,1,3]
list1*3
list2+3 and etc this named operation on the list 

"""
total = 0
count = 0
while(True):
    inp = input('Enter a number: ')
    assert int (inp) 
    if inp == 'done': break
    value = float(inp)
    total = total+ value
    count = count +1
    average = total / count

print('average:' , average)