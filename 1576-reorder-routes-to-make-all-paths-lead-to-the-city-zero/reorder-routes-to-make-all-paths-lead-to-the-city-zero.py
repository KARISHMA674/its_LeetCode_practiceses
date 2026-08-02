from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  
            graph[v].append((u, 0))  

        reorder_count = 0
        visited = [False] * n
        visited[0] = True
        queue = deque([0])

       
        while queue:
            curr = queue.popleft()
            for neighbor, cost in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    reorder_count += cost
                    queue.append(neighbor)

        return reorder_count
        