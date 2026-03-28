class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        maxFreq = 0
        result = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1

            maxFreq = max(maxFreq, count[idx])

            while (r - l + 1) - maxFreq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result