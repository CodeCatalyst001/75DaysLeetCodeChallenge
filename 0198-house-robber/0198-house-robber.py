class Solution:
    def rob(self, nums: List[int]) -> int:
        pre_2 = 0
        pre_1 = 0

        for num in nums:
            curr  = max(pre_1, pre_2 + num)
            pre_2 = pre_1
            pre_1 = curr

        return pre_1