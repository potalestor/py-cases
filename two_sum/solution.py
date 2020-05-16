
from typing import List
import unittest

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = len(nums)
        # for i in range(0, l-1):
        #     for j in range(1, l):
        #         if (i != j) and (nums[i] + nums[j] == target):
        #             return [i, j]
      residuals = {nums[0]: 0}
      for j in range(1, len(nums)):
        residual = target - nums[j]
        i = residuals.get(residual, None)
        if (i == None):
          residuals[nums[j]] = j
        else:
          return [i, j]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_2(self):
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_3(self):
        self.assertEqual(self.solution.twoSum([2, 5, 5, 11], 10), [1, 2])

    def test_4(self):
        self.assertEqual(self.solution.twoSum(
            [x for x in range(0, 25196, 2)], 16021), None)


if __name__ == "__main__":
    unittest.main()
