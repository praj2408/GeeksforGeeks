from collections import Counter
class Solution:
    def firstRepeated(self,arr):
        # code here 
        
        
        freq = Counter(arr)
        
        
        for i , num in enumerate(arr):
            if freq[num] > 1:
                return i+1
                
        return -1