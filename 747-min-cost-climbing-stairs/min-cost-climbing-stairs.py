class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        first,second=cost[0],cost[1]
        for i in range(2,len(cost)):
            current=cost[i] + min(first,second)
            first=second
            second=current
        return min(first,second)
