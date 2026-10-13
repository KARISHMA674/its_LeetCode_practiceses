class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted([x * x for x in nums])
        n = len(sq)
        
        
        half = n // 2
        
        return sum(sq[half:]) - sum(sq[:half])