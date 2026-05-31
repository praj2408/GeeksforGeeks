class Solution:
    def findUnion(self, a, b):
        # code here 
        
        result = set()
        
        
        result.update(a)
        result.update(b)
        
        result = list(result)
        
        return sorted(result)