import unittest
from maxSubArray import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test1(self):
        self.assertEqual(
            self.S.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6
        )


if __name__ == "__main__":
    unittest.main()
