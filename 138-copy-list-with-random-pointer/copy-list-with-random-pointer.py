"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        curr=head
        while curr:
            cloned = Node(curr.val, curr.next)
            curr.next = cloned
            curr = cloned.next

    
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        cloned_head = head.next
        while curr:
            cloned = curr.next
            curr.next = cloned.next
            if cloned.next:
                cloned.next = cloned.next.next
            curr = curr.next

        return cloned_head
        