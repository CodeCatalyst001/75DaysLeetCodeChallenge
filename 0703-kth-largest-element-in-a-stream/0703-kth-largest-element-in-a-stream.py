class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self._heap = []                      
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)   
        if len(self._heap) > self.k:
            heapq.heappop(self._heap)
        return self._heap[0]