
'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''
from typing import List
import bisect
import unittest

class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #   lo, hi = 0, len(nums) - 1
    #   while lo < hi:
    #     mid = (lo + hi) // 2
    #     if nums[mid] == target:
    #       return mid
    #     elif nums[mid] < target:
    #       lo = mid + 1
    #     else:
    #       hi = mid
    #   if lo == len(nums) - 1 and target > nums[-1]:
    #     return len(nums) 
    #   return lo
    
    def searchInsert(self, nums: List[int], target: int) -> int:
       return bisect.bisect_left(nums, target)
        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)

    def test_2(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)

    def test_3(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 7), 4)

    def test_4(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 0), 0)

if __name__ == '__main__':
    unittest.main()


