class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        
        smallest = float('inf')
        sec_smallest = float('inf')
        
        for num in arr:
            if num < smallest:
                sec_smallest = smallest
                smallest = num
            elif num < sec_smallest and num != smallest:
                sec_smallest = num
                
        if sec_smallest == float('inf'):
            return [-1]
        
        return [smallest, sec_smallest]
