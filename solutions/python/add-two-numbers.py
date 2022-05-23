import math
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.addTwoNum(l1, l2)

    def addTwoNum(self, l1, l2, carry):
        node = ListNode()
        node.val = (l1.val + l2.val) % 10
        tmpCarry = math.floor((l1.val + l2.val + carry) / 10)
        node.next = self.addTwoNum(l1.next, l2.next, tmpCarry)

        return node
