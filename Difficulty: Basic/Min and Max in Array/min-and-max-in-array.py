class Solution:
    def getMinMax(self, arr):
        # code here
        
        
        maximum = float('-inf')
        minimum = float('inf')
        
        
        for num in arr:
            if num > maximum:
                maximum = num
                
            if num < minimum:
                minimum = num
                
        return [minimum, maximum]
        