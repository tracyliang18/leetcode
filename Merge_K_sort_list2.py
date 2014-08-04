# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        while len(lists) != 1:
            i = 0
            l = len(lists)
            #print l
            while i < l:
                if i + 1 < l:
                    ml = self.merge(lists[i], lists[i+1])
                else:
                    ml = self.merge(lists[i], None)
                lists.append(ml)
                #print len(lists)
                i += 2
            lists = lists[l:]
            #print lists
        return lists[0]





    def merge(self, l1, l2):
        l = None
        if l1 or l2:
            if (l1 and not l2) or (l1 and l1.val < l2.val):
                l = l1
                l1 = l1.next
            else:
                l = l2
                l2 = l2.next
        else:
            return None
        head = l
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l = l.next
                l1 = l1.next
            else:
                l.next = l2
                l = l.next
                l2=l2.next
        if l1:
            l.next = l1
        elif l2:
            l.next = l2
        else:
            l.next = None
        #print "merge"
        #printlist(head)

        return head

def makelist(array):
    if len(array) > 0:
        head = ListNode(array[0])
    else:
        return None
    p=head
    for i in xrange(1,len(array)):
        p.next = ListNode(array[i])
        p=p.next
    p.next=None
    return head

def printlist(Node):
    print "printing list"
    while Node:
        print Node.val
        Node=Node.next

l1 = makelist([3,5,6,9])
l2 = makelist([6,9,10,14,20])
l3 = makelist([-1,7,8,10])
#printlist(l1)
#printlist(l2)
#printlist(l3)
so = Solution()
so.mergeKLists([l1,l2,l3])

