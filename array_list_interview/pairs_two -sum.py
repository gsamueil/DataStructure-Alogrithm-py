"""write a program to find all pairs of integers whose sum is equal to a given number"""
"""[2,6,3,9,11]  9----------->[6,3]"""
"""Given an array of integers nums and an integer target , return indicates of the two numbers such that they add up to target 
you may assume that each input would have exactly one solution, and you may not use the same element twice.
you can return the answer in any order.
Input :num=[2,7,11,15], target =9
output:[0,1]
output:because nums[0]+nums[1] == 9 , we return [0,1].
* Does array contain only positive or negative numbers ?
* what if the same pair repeats twice , should we print it every time?
* if the reverse of the pair is acceptable e.g. can we print both(4,1) and (1,4) if the given sum is 5.
* Do we need to print only distinct pairs? does (3,3) is a valid pair forgiven sum of 6?
* How big is the array?
"""
def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]== nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i,j)

nums=[2,3,5,7,8]
find_pairs(nums,8)