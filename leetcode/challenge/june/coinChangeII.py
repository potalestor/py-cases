'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3353/

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
 

Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

import unittest
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [1] + [0]*amount
        for coin in coins:
            for i in range(coin, amount+1):
                ways[i] += ways[i-coin]
        return ways[amount]



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.change(5, [1, 2, 5]), 4)

    def test_2(self):
        self.assertEqual(self.solution.change(3, [2]), 0)
    
    def test_3(self):
        self.assertEqual(self.solution.change(10, [10]), 1)

if __name__ == '__main__':
    unittest.main()
