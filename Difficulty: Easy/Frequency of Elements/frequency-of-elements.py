class Solution:
    def countFreq(self, arr):
        #code here
        
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) +1
            
        result = []
        
        for key, value in freq.items():
            
            result.append([key, value])
            
        return result