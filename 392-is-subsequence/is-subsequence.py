class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j=0,0
        len_s, len_t=len(s),len(t)

        while i<len_s and j<len_t:
            if s[i]== t[j]:
                i+=1
            j+=1
        return i==len_s        