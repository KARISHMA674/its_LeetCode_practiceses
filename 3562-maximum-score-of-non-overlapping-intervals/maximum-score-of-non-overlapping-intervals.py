from bisect import bisect_left

class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
      
        n = len(intervals)
        indexed_intervals = [
            (intervals[i][0], intervals[i][1], intervals[i][2], i) 
            for i in range(n)
        ]
        
        indexed_intervals.sort(key=lambda x: (x[0], x[1], x[3]))
        
        starts = [x[0] for x in indexed_intervals]
        
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, weight, orig_idx = indexed_intervals[i]
           
            next_idx = bisect_left(starts, r + 1)
            
            for k in range(1, 5):
                best_weight, best_indices = dp[i + 1][k]
                
                prev_weight, prev_indices = dp[next_idx][k - 1]
                cand_weight = prev_weight + weight
                cand_indices = sorted([orig_idx] + prev_indices)
                
               
                if cand_weight > best_weight:
                    dp[i][k] = (cand_weight, cand_indices)
                elif cand_weight == best_weight:
                    if not best_indices or cand_indices < best_indices:
                        dp[i][k] = (cand_weight, cand_indices)
                    else:
                        dp[i][k] = (best_weight, best_indices)
                else:
                    dp[i][k] = (best_weight, best_indices)
                    
        return dp[0][4][1]