class Solution(object):

  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not s or not t or len(s) < len(t):
      return ""

    target_count = Counter(t)
    required = len(target_count)

    window_count = {}
    formed = 0

    min_len = float("inf")
    best_range = (0, 0)

    left = 0
    for right, char in enumerate(s):
      
      window_count[char] = window_count.get(char, 0) + 1

      if char in target_count and window_count[char] == target_count[char]:
        formed += 1

      while left <= right and formed == required:
        current_len = right - left + 1
        if current_len < min_len:
          min_len = current_len
          best_range = (left, right)

        left_char = s[left]
        window_count[left_char] -= 1
        if (
            left_char in target_count
            and window_count[left_char] < target_count[left_char]
        ):
          formed -= 1

        left += 1

    return "" if min_len == float("inf") else s[best_range[0] : best_range[1] + 1]