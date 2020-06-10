'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3354/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''
import unittest


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) and (n & (n-1)==0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.isPowerOfTwo(1),
            True
        )

    def test_2(self):
        self.assertEqual(
            self.solution.isPowerOfTwo(16),
            True
        )
    def test_3(self):
        self.assertEqual(
            self.solution.isPowerOfTwo(218),
            False
        )

if __name__ == '__main__':
    unittest.main()
