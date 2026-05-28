class Solution:
    def countFreq(self, arr):
        #code here
        
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        
        result = []
        
        for key in freq:
            result.append([key, freq[key]])
            
        return result