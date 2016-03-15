#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    head = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
#test
def make_list(array):
    if len(array) == 0:
        return None
    head = ListNode(array[0])
    cur = head
    for n in array[1:]:
        cur.next = ListNode(n)
        cur = cur.next
    return head

def print_list(node):
    cur = node
    while cur:
        print cur.val,"->",
        cur = cur.next
    print

L = make_list([1,2,3,4,5])
sol = Solution()
print_list(L)
print_list(sol.removeElements(L,1))
