import unittest
from solution import Solution
from solution import ListNode


class TestListNode(unittest.TestCase):
    def test1(self):
        self.assertEqual(str(ListNode(2, ListNode())), '2->0', '2->0')

    def test2(self):
        self.assertEqual(
            str(ListNode(2, ListNode(0, ListNode(3)))), '2->0->3', '2->0->3')

    def test3(self):
        self.assertEqual(str(ListNode(2)), '2')

    def test4(self):
        self.assertEqual(ListNode.linkedList('2->4->3'),
                         ListNode.linkedList('2->4->3'), '2->4->3')

    def test5(self):
        self.assertNotEqual(ListNode.linkedList(
            '2->5->3'), ListNode.linkedList('2->4->3'), '2->5->3 != 2->4->3')


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test1(self):
        self.assertEqual(
            self.S.addTwoNumbers(
                ListNode.linkedList('2->4->3'), ListNode.linkedList('5->6->4')
            ),
            ListNode.linkedList('7->0->8')
        )
    def test2(self):
        self.assertEqual(
            self.S.addTwoNumbers(
                ListNode.linkedList('5'), ListNode.linkedList('5')
            ),
            ListNode.linkedList('0->1')
        )

if __name__ == "__main__":
    unittest.main()
