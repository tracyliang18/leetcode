# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        p1 = head
        p2 = head
        while p1 is not None and p2 is not None:
            p1 = p1.next
            p2 = p2.next
            if p2 is not None:
                p2 = p2.next
            else:
                return False
            if(p1 == p2):
                return True
        return False


a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a

so = Solution()
print so.hasCycle(a)
