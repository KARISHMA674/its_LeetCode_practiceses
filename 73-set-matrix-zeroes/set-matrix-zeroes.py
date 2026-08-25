class Solution(object):

  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][c] == 0 for c in range(n))
    first_col_has_zero = any(matrix[r][0] == 0 for r in range(m))

    
    for r in range(1, m):
      for c in range(1, n):
        if matrix[r][c] == 0:
          matrix[r][0] = 0
          matrix[0][c] = 0

    
    for r in range(1, m):
      for c in range(1, n):
        if matrix[r][0] == 0 or matrix[0][c] == 0:
          matrix[r][c] = 0

    
    if first_row_has_zero:
      for c in range(n):
        matrix[0][c] = 0

   
    if first_col_has_zero:
      for r in range(m):
        matrix[r][0] = 0
        