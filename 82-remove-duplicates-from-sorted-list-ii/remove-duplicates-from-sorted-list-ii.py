# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):

  def deleteDuplicates(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # Create a dummy node that precedes the head to handle edge cases
    # where the head itself contains duplicate values.
    dummy = ListNode(0, head)
    prev = dummy

    while head:
     
      if head.next and head.val == head.next.val:
        
        while head.next and head.val == head.next.val:
          head = head.next
        
        prev.next = head.next
      else:
        
        prev = prev.next

      head = head.next

    return dummy.next