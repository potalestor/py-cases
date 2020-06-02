import unittest
from uniquePaths import Solution


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


if __name__ == "__main__":
    unittest.main()
