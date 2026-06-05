class Solution:
    def toLower (self , s : str)-> str :
        #code here 
        
        t = ''.join(letter.lower() for letter in s)
        
        return t
        