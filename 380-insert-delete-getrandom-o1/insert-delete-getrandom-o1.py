import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.indices:
            return False
        
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            return False
        
        
        idx_to_remove = self.indices[val]
        last_element = self.nums[-1]
        
        self.nums[idx_to_remove] = last_element
        self.indices[last_element] = idx_to_remove
        
        self.nums.pop()
        del self.indices[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)