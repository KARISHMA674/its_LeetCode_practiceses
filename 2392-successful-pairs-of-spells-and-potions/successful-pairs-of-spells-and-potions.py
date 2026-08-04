class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        m=len(potions)
        res=[]
        for spell in spells:
            target=(success+spell-1)//spell
            left,right=0,m
            while left<right:
                mid=(left+right)//2
                if potions[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            res.append(m-left)
        return res                
                         
        