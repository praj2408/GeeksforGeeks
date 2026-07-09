class Solution:
	def maxProduct(self,arr):
		# code here
		max_prod = min_prod = ans = arr[0]
		
    	for num in arr[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
    
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
    
            ans = max(ans, max_prod)
    
        return ans
