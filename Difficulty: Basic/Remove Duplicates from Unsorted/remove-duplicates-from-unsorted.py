class Solution:
    def removeDuplicate(self, arr):
        # code here
        
        
        s = set()
        result = []
        
        for num in arr:
            if num not in s:
                s.add(num)
                result.append(num)
        return result
    

