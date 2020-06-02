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

'''


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