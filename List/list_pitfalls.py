"""error appear None when pass numpy to list"""

mylist = [2,4,3,1,5,7]
# mylist = mylist.sort()
# print(mylist)### None appear on the result to avoid this error make a copy of this list 
orig = mylist[:]
print(mylist.sort())
print(orig)
print(mylist)