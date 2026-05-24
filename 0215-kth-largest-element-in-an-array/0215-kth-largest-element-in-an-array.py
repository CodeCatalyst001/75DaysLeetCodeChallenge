class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        OFFSET = 10000
        RANGE = 20001  
        count = [0] * RANGE
        for num in nums:
            count[num + OFFSET] += 1
        
        accumulated = 0
        for i in range(RANGE - 1, -1, -1):
            accumulated += count[i]
            if accumulated >= k:
                return i - OFFSET
        
        return -1 