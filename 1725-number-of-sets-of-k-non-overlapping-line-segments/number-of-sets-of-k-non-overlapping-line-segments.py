class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        MOD=10**9+7
        total_n=n+k-1
        r=2*k

        if r>total_n:
            return 0

        num=1
        den=1
        for i in range(1,r+1):
            num=(num*(total_n-i+1)) % MOD
            den=(den *i) %MOD

        return (num* pow(den,MOD -2,MOD)) % MOD    
