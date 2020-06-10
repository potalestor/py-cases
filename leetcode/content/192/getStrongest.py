import unittest
'''

'''
from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = (len(arr)- 1)>>1
        sarr = [[x, 0] for x in sorted(arr)]
        sm = sarr[m][0]
        sarr.reverse()
        for i  in range(len(arr)):
            sarr[i][1] = sarr[i][0] - sm if sarr[i][0] - sm > 0 else sm - sarr[i][0]
        sarr = sorted(sarr, key = lambda x: -x[1])
        return [x[0] for i, x in enumerate(sarr) if i < k]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.getStrongest([1,2,3,4,5], 2), [5,1])
    def test_2(self):
        self.assertEqual(self.solution.getStrongest([1,1,3,5,5], 2), [5,5])
    def test_3(self):
        self.assertEqual(self.solution.getStrongest([6,7,11,7,6,8], 5), [11,8,6,6,7])
    def test_4(self):
        self.assertEqual(self.solution.getStrongest([6,-3,7,2,11], 3), [-3,11,2])
    def test_5(self):
        self.assertEqual(self.solution.getStrongest([-7,22,17,3], 2), [22,17])

if __name__ == '__main__':
    unittest.main()
