from typing import List

# Definition for singly-linked list.
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