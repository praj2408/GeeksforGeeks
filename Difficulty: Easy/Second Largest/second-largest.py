class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        
        largest = arr[0]
        sec_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                sec_largest = largest
                largest = num
                
            elif num > sec_largest and num != largest:
                sec_largest = num
                
        if  sec_largest == float('-inf'):
            return -1
                
        return sec_largest
        