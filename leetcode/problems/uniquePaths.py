'''
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Input: m = 7, n = 3
Output: 28

https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''
from typing import List
import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[1] * m for i in range(n)]
        print(a)
        ''' rows '''
        for i in range(1, n):
            ''' cols '''
            for j in range(1, m):
                # print("before:", a)
                a[i][j] = a[i][j-1] + a[i-1][j]
                # print("after:", a)
        return a[n-1][m-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if (obstacleGrid[0][0] == 1):
            return 0
        obstacleGrid[0][0] = 1
        print("before:", obstacleGrid)
        for i in range (len(obstacleGrid)):
            if (i == 0):
                for j in range (1, len(obstacleGrid[0])):
                    if (obstacleGrid[i][j] == 1) or (obstacleGrid[i][j-1] == 0):
                        obstacleGrid[i][j] = 0
                    else: 
                        obstacleGrid[i][j] = 1 
            else:
                if (obstacleGrid[i][0] == 1) or (obstacleGrid[i-1][0] == 0):
                        obstacleGrid[i][0] = 0
                else: 
                    obstacleGrid[i][0] = 1                                
        print("after:", obstacleGrid)

        for i in range (1, len(obstacleGrid)):
            print("before:", obstacleGrid)
            for j in range (1, len(obstacleGrid[i])):
                if (obstacleGrid[i][j] == 1):
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1] - obstacleGrid[i][j]

            print("after:", obstacleGrid)

        return obstacleGrid[-1][-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test1(self):
        self.assertEqual(
            self.S.uniquePaths(3, 2),
            3
        )

    def test2(self):
        self.assertEqual(
            self.S.uniquePaths(7, 3),
            28
        )

    def test3(self):
        self.assertEqual(
            self.S.uniquePathsWithObstacles([
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]),
            2
        )
    def test4(self):
        self.assertEqual(
            self.S.uniquePathsWithObstacles([
                [1, 0]
            ]),
            0
        )
    def test5(self):
        self.assertEqual(
            self.S.uniquePathsWithObstacles([
                [0,0],
                [1,1],
                [0,0]
            ]),
            0
        )

if __name__ == "__main__":
    unittest.main()
