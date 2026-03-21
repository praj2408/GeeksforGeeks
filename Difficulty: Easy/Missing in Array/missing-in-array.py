class Solution:
    def missingNum(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        actual_sum = (n + 1) * (n + 2) // 2
        return actual_sum - total_sum