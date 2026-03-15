class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            id = abs(x) - 1
            if nums[id] >0:
                nums[id] = -nums[id]
        return[i+1 for i, v in enumerate(nums) if v > 0]