"""Is unique \contain Duplicate leetcode 217"""
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

step-1 create empty list
step-2 loop through given list
step-3 in each visit check if the  vist element is in our newly created list and save the visited element in the newly created list
"""
# nums = [0, 2, 3, 1]

# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """

#         a = []
#         for i in nums:
#             if i in a:
#                 print(i)
#                 return True
#             else:
#                 a.append(i)
#         return False
# time consuming on this solution very large we will solve it by hashing
# another solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
