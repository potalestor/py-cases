'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
import unittest
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
      result = []
      for i in sorted(people, key = lambda x: (-x[0], x[1])):
          result.insert(i[1], i)
      return result
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):

        self.solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
        self.assertEqual(
            self.solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]),
            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
            )




if __name__ == '__main__':
    unittest.main()

