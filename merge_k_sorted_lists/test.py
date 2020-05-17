import unittest
from solution import Solution
from solution import ListNode

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test1(self):
        self.assertEqual(
            self.S.mergeKLists([
                ListNode.linkedList('1->4->5'), 
                ListNode.linkedList('1->3->4'),
                ListNode.linkedList('2->6')
            ]),
            ListNode.linkedList('1->1->2->3->4->4->5->6')
        )


if __name__ == "__main__":
    unittest.main()