import unittest
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def linkedList(cls, s:str):
        list = s.split('->')
        if len(list) == 0:
            return
        root = cls(int(list[0]))
        node = root
        for i in range (1, len(list)):
            node.next = cls(int(list[i]))
            node = node.next
        return root
     
    def __str__(self):
        result = '{0}'.format(self.val)
        node = self.next
        while node:
            result += '->{0}'.format(node.val)
            node = node.next
        return result
    
    def __eq__(self, other):
        return (self.val == other.val) and (self.next.__eq__(other.next))


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

if __name__ == "__main__":
    unittest.main()