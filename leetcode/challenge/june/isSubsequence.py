'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/

Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
'''
import unittest


class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
        # i = j = 0
        # while((i < len(s)) and (j < len(t))):
        #     if s[i] == t[j]:
        #         i +=1
        #     j +=1
        # return i == len(s)

    def isSubsequence(self, s, target):
        iter_target = iter(target)
        return all(char in iter_target for char in s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(
            self.solution.isSubsequence("abc", "ahbgdc"),
            True
        )

    def test_2(self):
        self.assertEqual(
            self.solution.isSubsequence("axc", "ahbgdc"),
            False
        )
    def test_3(self):
        self.assertEqual(
            self.solution.isSubsequence("", "ahbgdc"),
            True
        )

if __name__ == '__main__':
    unittest.main()

