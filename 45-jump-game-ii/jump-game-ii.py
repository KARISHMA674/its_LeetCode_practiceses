class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        if n<=1:
            return 0
        jumps=0
        cur_end=0
        farthest=0


        for i in range(n-1):
            farthest=max(farthest, i +nums[i])

            if i == cur_end:
                jumps+=1
                cur_end=farthest

                if cur_end >=n-1:
                    break
        return jumps                
        