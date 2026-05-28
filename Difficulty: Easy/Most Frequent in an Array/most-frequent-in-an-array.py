class Solution:
    def mostFreqEle(self, arr):
        # code here
        
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
        max_freq = max(freq.values())
            
        
        result = max(k for k, v in freq.items() if v == max_freq)
        
        return result