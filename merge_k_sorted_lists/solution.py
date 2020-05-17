from typing import List

'''
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

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


class MinHeap:
    def __init__(self, list: List[ListNode]):
        self.__heap = list
        self.__size = len(list)
        for i in range(self.__size >> 1, -1, -1):
            self.__minHeapify(i)

    def __minHeapify(self, i):
        li = 2*i + 1
        ri = 2*i + 2
        si = i
        if li < self.__size and self.__heap[i].val > self.__heap[li].val:
            si = li
        if ri < self.__size and self.__heap[si].val > self.__heap[ri].val:
            si = ri
        if si != i:
            self.__heap[i], self.__heap[si] = self.__heap[si], self.__heap[i]
            self.__minHeapify(si)

    def min(self):
        if self.__size > 0:
            return self.__heap[0]
        return None

    def replaceMin(self, item):
        self.__heap[0] = item
        self.__minHeapify(0)

    def deleteMin(self):
        if self.__size < 0:
            return
        self.__heap[0] = self.__heap[-1]
        del self.__heap[-1]
        self.__size -= 1
        self.__minHeapify(0)




class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        tail = None
        minHeap = MinHeap([node for node in lists if node is not None])
        while True:
            min = minHeap.min()
            if min is None:
                return head

            if head is None:
                head = ListNode(min.val)
                tail = head
            else:
                tail.next = ListNode(min.val)
                tail = tail.next
            if min.next is None:
                minHeap.deleteMin()
            else:
                minHeap.replaceMin(min.next)
