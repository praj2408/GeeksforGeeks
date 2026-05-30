class Solution:
    def largest(self, arr):
        # code here
        
        maxi = float('-inf')
        
        for num in arr:
            if num > maxi:
                maxi = num
                
        return maxi
