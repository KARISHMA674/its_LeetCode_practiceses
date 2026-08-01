class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)
                
        return provinces
        