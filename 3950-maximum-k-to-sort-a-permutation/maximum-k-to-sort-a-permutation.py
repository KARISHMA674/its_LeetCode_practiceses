class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        for i, val in enumerate(nums):
            if i != val:
                ans &= val

        return max(ans, 0)