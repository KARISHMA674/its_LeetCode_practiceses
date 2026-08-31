# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_cp_index = -1
        last_cp_index = -1
        prev_cp_index = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 1  
        

        while curr.next:
            
            is_maxima = prev.val < curr.val and curr.val > curr.next.val
            is_minima = prev.val > curr.val and curr.val < curr.next.val

            if is_maxima or is_minima:
                if first_cp_index == -1:
                    first_cp_index = index
                else:
                    min_dist = min(min_dist, index - prev_cp_index)

                prev_cp_index = index
                last_cp_index = index

            prev = curr
            curr = curr.next
            index += 1

        if first_cp_index == last_cp_index:
            return [-1, -1]

        max_dist = last_cp_index - first_cp_index
        return [min_dist, max_dist]
        