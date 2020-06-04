from typing import List
import bisect

'''
https://leetcode.com/problems/3sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
import unittest

class Solution:
    # Runtime: 196 ms, faster than 99.92% of Python3 online submissions for 3Sum.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0. Result list
        solution = []
        
        # 1. Create a dictionary from duplicates list
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        # 2. Creatу a sorted list from dictionary keys 
        nums=sorted(dic)
  
        # 3. Iterating ...
        for i, num1 in enumerate(nums):

            # The private solutions to the problem:
            if num1 == 0:
                # The second private solution to the problem:
                # if 0 met in the list more then 2 times     
                if dic[num1] > 2:
                    solution.append((0, 0, 0))
            else:
                # The second private solution to the problem: 
                # if a one number duplicate has doubled opposite number
                if dic[num1] > 1 and -2 * num1 in dic:
                    solution.append((num1, num1, -2 * num1))

            # The general solution to the problem:
            if num1 < 0:
                # for example: we have [-5, 0, 1, 2, 3, 4, 5]. Current num = -5, then target = 5
                target = - num1
                # find a place to insert an element into a sorted list, so that elem is located to the left
                # probable min num2 is target-nums[-1] = 5 - 5 == 0, i + 1 == 1
                # left == 1
                left = bisect.bisect_left(nums, target-nums[-1], i + 1)
                # probable max num2 is target >> 1 == 2 
                # right == 4 (2 in position 3)
                right = bisect.bisect_right(nums, target >> 1, left)
                # find concrete num2 in slice
                for num2 in nums[left : right]:
                    # find concrete num3
                    num3 = target - num2
                    # check num3 in dic
                    if num3 in dic and num2 != num3:
                        solution.append((num1, num2, num3))

        return solution

# 	 Runtime: 2320 ms, faster than 6.85% of Python3 online submissions for 3Sum.	
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         triplets = set()

#         print("basic list", nums)
#         # we need to sort list
#         nums.sort()
#         print("sorted list", nums)

#         # then create a for loop.
#         # this loop is going to represent a number that we are comparing everything to

#         # i = number we aren't changing
#         # j = low pointer start spot
#         # k = high pointer start spot

#         for i in range(0, len(nums) - 1):
#             j = i + 1
#             k = len(nums) - 1
#             while (j < k):
#                 sum = nums[i] + nums[j] + nums[k]
#                 if (sum == 0):
#                     triplet = (nums[i], nums[j], nums[k])
#                     triplets.add(triplet)
#                     # if triplet not in triplets:
#                     #     triplets.append(triplet)
#                     j = j + 1
#                     k = k - 1
#                 else:
#                     if (sum < 0):
#                         j = j + 1
#                     else:
#                         k = k - 1
#         # print("triplets", triplets)
#         return [ x for x in triplets ]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_1(self):
        self.assertEqual(self.solution.threeSum([-5, 0, 1, 2, 3, 4, 5]), [(-5, 0, 5), (-5, 1, 4), (-5, 2, 3)])    

    def test_2(self):
        self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [(-1, -1, 2), (-1, 0, 1)])





if __name__ == "__main__":
    unittest.main()
