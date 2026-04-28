class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        X = None
        count = 0

        for num in nums:
            if count == 0 :
                X = num
            count += (1 if num == X else -1)

        return X