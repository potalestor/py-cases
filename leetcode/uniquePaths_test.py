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
