class Solution(object):

  def minAddToMakeValid(self, s):
    """
    :type s: str
    :rtype: int
    """
    open_count = 0  
    insertions = 0  
    for char in s:
      if char == "(":
        open_count += 1
      else:  
        if open_count > 0:
          open_count -= 1 
        else:
          insertions += 1  

    
    return insertions + open_count