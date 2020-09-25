# Definition for singly-linked list.
class ListNode:
      def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(val=0, next=None)
        rear = res
        while(l1 and l2):
                rear.next = l1 if(l1.val<=l2.val) else l2

                if(l1.val<=l2.val):
                    l1 = l1.next
                else:
                    l2 = l2.next
                rear = rear.next
        rear.next = l1 if l1 else l2
        return res.next