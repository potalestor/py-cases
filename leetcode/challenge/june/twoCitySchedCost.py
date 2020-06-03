'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3349/

There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
'''

import unittest
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       costs = sorted(costs, key=lambda x: x[0] - x[1])
       n = len(costs)
       return sum(costs[i][0] for i in range(n//2)) + sum(costs[i][1] for i in range(n//2,n))
 
    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    #     sum = 0
    #     costs.sort(key=lambda x: x[0]-x[1])
    #     m = len(costs)
    #     for i in range(m):
    #         sum += costs[i][0] if i < m//2 else costs[i][1]
    #     return sum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.twoCitySchedCost([
            [10, 20],
            [30, 200],
            [400, 50],
            [30, 20]
        ]), 110)

    def test_2(self):
        self.assertEqual(self.solution.twoCitySchedCost([
            [259, 770],
            [448, 54],
            [926, 667],
            [184, 139],
            [840, 118],
            [577, 469]
        ]), 1859)


if __name__ == '__main__':
    unittest.main()
