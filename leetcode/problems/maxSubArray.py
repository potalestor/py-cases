'''
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
import unittest
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMaxSum = globalMaxSum = nums[0]
        for i in range (1, len(nums)):
            currentMaxSum = max(nums[i], currentMaxSum + nums[i])
            globalMaxSum = max(currentMaxSum, globalMaxSum)
        return globalMaxSum

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test1(self):
        self.assertEqual(
            self.S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6
        )


if __name__ == "__main__":
    unittest.main()
