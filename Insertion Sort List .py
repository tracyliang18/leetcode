# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return None
        p = head
        q = p.next
        while q:
            if q.val >= p.val:
                p = q
                q = q.next
            else:
                p.next = q.next
                r = head
                last = None
                while q.val >= r.val:
                    last = r
                    r = r.next
                if last is None:
                    head = q
                else:
                    last.next = q
                q.next = r
                q = p.next
        return head



n1 = ListNode(1)
n2 = ListNode(6)
n3 = ListNode(2)
n4 = ListNode(9)
n5 = ListNode(4)

so = Solution()
head = so.insertionSortList(n1)
while head is not None:
    print head.val
    head = head.next







