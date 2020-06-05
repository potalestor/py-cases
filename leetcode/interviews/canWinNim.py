import unittest
'''


'''


class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n%4==0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.canWinNim(4), False)

    def test_2(self):
        self.assertEqual(self.solution.canWinNim(3), True)

    def test_3(self):
        self.assertEqual(self.solution.canWinNim(5), True)

    def test_4(self):
        self.assertEqual(self.solution.canWinNim(6), True)
    
    def test_5(self):
        self.assertEqual(self.solution.canWinNim(7), True)


if __name__ == '__main__':
    unittest.main()
