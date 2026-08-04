class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left,right=1,max(piles)
        while left<right:
            mid =(left+right)//2
            total_hours=sum((p+mid-1)//mid for p in piles)
            if total_hours<=h:
                right=mid
            else:
                left=mid+1
        return left           
        