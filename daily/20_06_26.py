# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        li = []
        this = head
        while this.next != None:
            if not this.val in li:
                li.append(this.val)
                this = this.next
            else:
                this = this.next.next
        return li

if __name__ == "__main__":
    app = Solution()
    print(app.removeDuplicateNodes([1, 1, 1, 1, 2]))