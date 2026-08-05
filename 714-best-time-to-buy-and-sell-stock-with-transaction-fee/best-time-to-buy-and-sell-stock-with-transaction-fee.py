class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        hold=-prices[0]
        free=0
        for price in prices[1:]:
            hold=max(hold,free-price)
            free=max(free,hold+price-fee)

        return free    

        