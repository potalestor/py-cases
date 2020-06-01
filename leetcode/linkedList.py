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