class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_p = 0
        for price in prices:
            if price < min_p:
                min_p = price
            else:
                profit = price - min_p
                max_p = max (max_p,profit)
        return max_p