# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        head = self.getCurMin(lists)
        p = head
        while p:
            p.next=self.getCurMin(lists)
            p=p.next
        return head


    def getCurMin(self, lists):
        curmin = None
        pos = None
        for ind,l in enumerate(lists):
            if l :
                if curmin == None or l.val < curmin.val:
                    pos = ind
                    curmin = l
        if curmin:
            lists[pos] = lists[pos].next
        return curmin
