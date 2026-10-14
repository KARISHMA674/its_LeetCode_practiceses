class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum >9*num:
            return ""

        nines=sum//9
        rem=sum%9

        res=["9"*nines]
        if rem>0:
            res.append(str(rem))

        remaining_zeros=num-nines-(1 if rem>0 else 0)
        if remaining_zeros>0:
            res.append("0" * remaining_zeros)


        return "".join(res)            