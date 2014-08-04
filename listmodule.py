# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
