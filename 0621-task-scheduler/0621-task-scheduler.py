class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = Counter(tasks)        
        f_max = max(freq.values())
        k = sum(1 for v in freq.values() if v == f_max)
        part = (f_max - 1) * (n + 1) + k
        return max(part, len(tasks))
        