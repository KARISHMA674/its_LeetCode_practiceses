class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = 0
                    queue = [(r, c)]
                    island_sum += grid[r][c]
                    grid[r][c] = 0  
                    
                    head = 0
                    while head < len(queue):
                        curr_r, curr_c = queue[head]
                        head += 1
                        
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  
                                queue.append((nr, nc))
                    
                    if island_sum % k == 0:
                        count += 1
                        
        return count