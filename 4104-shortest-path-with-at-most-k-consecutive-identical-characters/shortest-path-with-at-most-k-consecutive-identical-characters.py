import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        if k < 1:
            return -1
        
        if n == 1:
            return 0
        
        adj = [[] for _ in range(n)]
        for edge in edges:
            u, v, w = edge[0], edge[1], edge[2]
            adj[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, consec = heapq.heappop(pq)
            
            if d > dist[u][consec]:
                continue
            
            if u == n - 1:
                return d
            
            for v, w in adj[u]:
                new_consec = consec + 1 if labels[v] == labels[u] else 1
                if new_consec <= k and d + w < dist[v][new_consec]:
                    dist[v][new_consec] = d + w
                    heapq.heappush(pq, (d + w, v, new_consec))
                        
        return -1