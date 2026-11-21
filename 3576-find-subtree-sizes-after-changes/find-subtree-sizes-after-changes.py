class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        ans = [1] * n
        last_seen = {}
        
        def dfs(u):
            char = s[u]
            prev_ancestor = last_seen.get(char, -1)
            
            new_p = prev_ancestor if prev_ancestor != -1 else parent[u]
            
            last_seen[char] = u
            
            for v in adj[u]:
                child_new_p = dfs(v)
                if child_new_p != -1:
                    ans[child_new_p] += ans[v]
                    
            if prev_ancestor == -1:
                del last_seen[char]
            else:
                last_seen[char] = prev_ancestor
                
            return new_p

        dfs(0)
        return ans