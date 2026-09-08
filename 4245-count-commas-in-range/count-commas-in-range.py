class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total=0
        threshold=1000
        while n>= threshold:
            total += n-threshold +1
            threshold *=1000
        return total    