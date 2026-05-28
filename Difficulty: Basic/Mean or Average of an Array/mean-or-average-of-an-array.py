class Solution:
    def findMean(self, arr):
        # code here 
        
        
        
        summation = sum(arr)
        n = len(arr)
        
        average = int(summation / n)
        
        return average