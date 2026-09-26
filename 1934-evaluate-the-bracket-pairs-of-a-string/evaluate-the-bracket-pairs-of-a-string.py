class Solution(object):

  def evaluate(self, s, knowledge):
    """
    :type s: str
    :type knowledge: List[List[str]]
    :rtype: str
    """
    
    mapping = {k: v for k, v in knowledge}

    result = []
    in_bracket = False
    current_key = []

    for ch in s:
      if ch == "(":
        in_bracket = True
        current_key = []
      elif ch == ")":
        in_bracket = False
        key_str = "".join(current_key)
       
        result.append(mapping.get(key_str, "?"))
      else:
        if in_bracket:
          current_key.append(ch)
        else:
          result.append(ch)

    return "".join(result)