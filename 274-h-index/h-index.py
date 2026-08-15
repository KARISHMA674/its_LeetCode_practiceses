class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0] * (n + 1)
        
        
        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
                
      
        total = 0
        for h in range(n, -1, -1):
            total += buckets[h]
            if total >= h:
                return h
                
        return 0


        
        