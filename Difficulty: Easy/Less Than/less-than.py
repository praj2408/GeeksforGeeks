class Solution:

    def lessThan(self, arr, k):
        #code here
        
        result = []
        
        for num in arr:
            if num < k:
                result.append(num)
    
        return result