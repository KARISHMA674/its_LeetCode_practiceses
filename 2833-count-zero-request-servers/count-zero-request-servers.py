from collections import defaultdict

class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda log: log[1])
        
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        server_counts = defaultdict(int)
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for orig_idx, q in sorted_queries:
            while right < num_logs and logs[right][1] <= q:
                server_counts[logs[right][0]] += 1
                right += 1
            
            while left < num_logs and logs[left][1] < q - x:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1
            
            ans[orig_idx] = n - len(server_counts)
            
        return ans