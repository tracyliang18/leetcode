# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head is None:
            return None
        while 1:
            p = head;q = None; r = None; s = None;head2 = None; l = None;
            ok = True
            while p is not None:
                q = p
                while q.next is not None and q.val <= q.next.val:
                    q = q.next
                q = q.next
                if q is not None:
                    ok = False
                r = s = q
                if q is not None:
                    while s.next is not None and s.val <= s.next.val:
                        s = s.next
                    s = s.next
                while p != q or r != s:
                    if r == s or p != q and p.val < r.val:
                        if l is None:
                            head2 = p
                        else:
                            l.next = p
                        l = p
                        p=p.next
                    else:
                        if l is None:
                            head2 = r
                        else:
                            l.next = r
                        l = r
                        r = r.next
                p = s
            l.next = None
            head = head2
            if ok:
                break
        return head




n1 = ListNode(1)
n2 = ListNode(6)
n3 = ListNode(2)
n4 = ListNode(9)
n5 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None

so = Solution()
head = so.sortList(n1)
while head is not None:
    print head.val
    head = head.next