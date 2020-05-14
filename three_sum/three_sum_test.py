import unittest
from three_sum import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_1(self):
        self.assertEqual(self.solution.threeSum([-5, 0, 1, 2, 3, 4, 5]), [[-5, 0, 5]])    


    # def test_2(self):
    #     self.assertEqual(self.solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])





if __name__ == "__main__":
    unittest.main()
