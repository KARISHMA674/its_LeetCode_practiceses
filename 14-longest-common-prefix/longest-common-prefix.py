class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        first = strs[0]
        for i in range(len(first)):
            char=first[i]
            for s in strs[1:]:

                if i ==len(s) or s[i] != char:
                    return first[:i]

        return first                
        