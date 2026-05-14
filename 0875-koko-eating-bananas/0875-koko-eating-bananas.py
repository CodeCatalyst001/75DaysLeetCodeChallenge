class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours_needed = 0
            
        
            for pile in piles:
                hours_needed += (pile + mid - 1) // mid 
            
            
            if hours_needed <= h:
                right = mid  
            else:
                left = mid + 1  
        
        return left