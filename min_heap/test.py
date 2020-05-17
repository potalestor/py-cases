import unittest
from realization import MinHeap

class TestRealization(unittest.TestCase):

    def testMinHeap1(self):
        h = MinHeap([1, 2, 3, 4, 5])
        self.assertEqual(h.min(), 1)
    def testMinHeap2(self):
        h = MinHeap([5, 4, 3, 2, 1])
        self.assertEqual(h.min(), 1)
    def testMinHeap3(self):
        h = MinHeap([3, 4, 3, 5, 8, 10, 1, 4, 2, 9, 10])
        self.assertEqual(h.min(), 1)

    def testReplaceMin(self):
        h = MinHeap([3, 4, 7, 5, 8, 11, 1, 6, 2, 9, 10])
        self.assertEqual(h.min(), 1)
        h.replaceMin(12)
        self.assertEqual(h.min(), 2)
        h.replaceMin(13)
        self.assertEqual(h.min(), 3)

    def testPop(self):
        h = MinHeap([3, 4, 7])
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(h.pop(), 7)
        self.assertEqual(h.pop(), None)

if __name__ == "__main__":
    unittest.main()