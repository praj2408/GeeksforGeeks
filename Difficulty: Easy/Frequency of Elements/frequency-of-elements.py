from collections import Counter

class Solution:
    def countFreq(self, arr):
        #code here
        
        
        freq = Counter(arr)
        
        result = []
        for num, count in freq.items():
            result.append([num, count])
            
        return result