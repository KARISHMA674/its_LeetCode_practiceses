from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
       
        graph = defaultdict(list)
        for (u, v), val in zip(equations, values):
            graph[u].append((v, val))
            graph[v].append((u, 1.0 / val))

        def dfs(curr, target, visited):
            
            if curr == target:
                return 1.0

            visited.add(curr)
            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return res * weight

            return -1.0

        results = []
        for src, dst in queries:
           
            if src not in graph or dst not in graph:
                results.append(-1.0)
            elif src == dst:
                results.append(1.0)
            else:
                results.append(dfs(src, dst, set()))

        return results