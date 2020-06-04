import unittest
'''
https://leetcode.com/problems/climbing-stairs/submissions/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''


class Solution:
    def climbStairs(self, n: int) -> int:
        ''' Hi Leonardus Pisanus (Fibonacci Sequence)! '''
        m = [x+1 for x in range(n)]
        for i in range(2, n):
            m[i] = m[i-1]+m[i-2]
        return m[n-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_2(self):
        self.assertEqual(self.solution.climbStairs(3), 3)


if __name__ == '__main__':
    unittest.main()
