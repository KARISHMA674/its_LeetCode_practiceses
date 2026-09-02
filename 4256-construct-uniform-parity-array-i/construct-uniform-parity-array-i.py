class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        
        has_even = any(x % 2 == 0 for x in nums1)
        has_odd = any(x % 2 != 0 for x in nums1)

        if not has_even or not has_odd:
            return True

        return True 