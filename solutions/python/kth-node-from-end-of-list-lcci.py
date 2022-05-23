# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        s = []
        res = 0
        rear = head
        while(rear):
            s.append(rear.val)
            rear = rear.next
        
        for i in range(k):
            res = s.pop()
        
        return res