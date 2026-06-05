class Solution:
    def majorityElement(self, arr):
        #code here
        
        freq = {}
        
        
        for num in arr:
            freq[num] = freq.get(num, 0) +1
            
            if freq[num] > (len(arr)//2):
                return num
                
        return -1