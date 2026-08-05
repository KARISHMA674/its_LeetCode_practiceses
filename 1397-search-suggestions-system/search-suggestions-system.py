class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []  

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        
        root = TrieNode()
        
       
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                
                
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)
        
        result = []
        curr = root
        for char in searchWord:
            if curr and char in curr.children:
                curr = curr.children[char]
                result.append(curr.suggestions)
            else:
                curr = None  
                result.append([])
                
        return result        