'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
   Hide Hint #1  
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
'''

import unittest
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

    # def reverseString(self, s: List[str]):
    #     l = len(s)
    #     n = l//2
    #     for i in range(n):
    #         s[i], s[l-i-1] = s[l-i-1], s[i]

    # def reverseString(self, s: List[str]):
    #     for i in range(len(s) // 2):
    #         s[i], s[-i - 1] = s[-i - 1], s[i]

    def reverseString(self, l: List[str]) -> None:
        i=0
        j=len(l)-1
        while(i<j):
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        s = ["h","e","l","l","o"]
        rs = s[::-1]
        self.solution.reverseString(s)
        self.assertEqual(s, rs)

    def test_2(self):
        s = ["H","a","n","n","a","h"]
        rs = s[::-1]
        self.solution.reverseString(s)
        self.assertEqual(s, rs)


if __name__ == '__main__':
    unittest.main()
