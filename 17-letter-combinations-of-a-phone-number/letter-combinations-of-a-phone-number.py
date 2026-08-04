class Solution(object):

  def letterCombinations(self, digits):
    if not digits:
      return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = [""]

    for digit in digits:
      temp = []
      for combination in res:
        for letter in phone_map[digit]:
          temp.append(combination + letter)
      res = temp

    return res
        