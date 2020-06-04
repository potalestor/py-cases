from typing import List


'''
https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

import unittest
from linkedList import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # remainder of dividing by 10
        rem = 0
        root = None
        tail = None
        while (l1 or l2):
            sum = rem
            if l1:
                sum += l1.val  
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            if sum >= 10:
                rem = 1
                node = ListNode(sum % 10)
            else:
                rem = 0
                node = ListNode(sum)
                
            if root:
                tail.next = node
                tail = node
            else:
                root = node
                tail = node
                
        if rem > 0:
            tail.next = ListNode(rem)        
        return root


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
