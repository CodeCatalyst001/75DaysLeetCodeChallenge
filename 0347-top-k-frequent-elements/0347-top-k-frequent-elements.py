from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result