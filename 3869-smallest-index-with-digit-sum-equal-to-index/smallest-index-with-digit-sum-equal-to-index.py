class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            
            digit_sum = sum(int(d) for d in str(nums[i]))
            
            
            if i == digit_sum:
                return i
        
        
        return -1