class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        distance_value = 0
        n = len(arr2)
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            
            if idx == n or arr2[idx] > x + d:
                distance_value += 1
                
        return distance_value