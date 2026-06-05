from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       
        if len(s1) != len(s2):
           return False
           
        count = Counter(s1)
        
        for char in s2:
            if count[char] == 0:
                return False
            count[char] -= 1
            
        return True