
class Solution:

    def checkDuplicates(self, arr):
        #code here
        
        s = set()
        for num in arr:
            s.add(num)
        
        return len(arr) != len(s)
