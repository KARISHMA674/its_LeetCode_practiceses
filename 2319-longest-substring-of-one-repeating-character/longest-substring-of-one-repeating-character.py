class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = list(s)
        
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.left_char = [''] * (4 * self.n)
        self.right_char = [''] * (4 * self.n)
        
        self._build(1, 0, self.n - 1)

    def _merge(self, node, left_child, right_child, l_len, r_len):
        self.left_char[node] = self.left_char[left_child]
        self.right_char[node] = self.right_char[right_child]
        
        if self.pref_len[left_child] == l_len and self.left_char[left_child] == self.left_char[right_child]:
            self.pref_len[node] = l_len + self.pref_len[right_child]
        else:
            self.pref_len[node] = self.pref_len[left_child]
            
        if self.suff_len[right_child] == r_len and self.right_char[left_child] == self.right_char[right_child]:
            self.suff_len[node] = r_len + self.suff_len[left_child]
        else:
            self.suff_len[node] = self.suff_len[right_child]
            
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])
        if self.right_char[left_child] == self.left_char[right_child]:
            self.max_len[node] = max(
                self.max_len[node], 
                self.suff_len[left_child] + self.pref_len[right_child]
            )

    def _build(self, node, start, end):
        if start == end:
            char = self.s[start]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.left_char[node] = char
            self.right_char[node] = char
            return
        
        mid = (start + end) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        self._merge(node, left_child, right_child, mid - start + 1, end - mid)

    def update(self, node, start, end, idx, char):
        if start == end:
            self.s[idx] = char
            self.left_char[node] = char
            self.right_char[node] = char
            return
            
        mid = (start + end) // 2
        left_child, right_child = 2 * node, 2 * node + 1
        
        if idx <= mid:
            self.update(left_child, start, mid, idx, char)
        else:
            self.update(right_child, mid + 1, end, idx, char)
            
        self._merge(node, left_child, right_child, mid - start + 1, end - mid)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        tree = SegmentTree(s)
        ans = []
        n = len(s)
        
        for char, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, n - 1, idx, char)
            
            ans.append(tree.max_len[1])
            
        return ans