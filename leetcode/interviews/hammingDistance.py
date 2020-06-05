'''


'''
import unittest


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Find different bits
        xor = x ^ y
        result = 0
        while(xor > 0):
            # Sum different bits
            if (xor & 1 == 1):
                result += 1
            xor >>= 1
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.hammingDistance(1, 4), 2)


if __name__ == '__main__':
    unittest.main()
