class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        max_length = 0

        for right, char in enumerate(s):
            left = max(left, last_seen[ord(char)] + 1)
            last_seen[ord(char)] = right
            max_length = max(max_length, right - left + 1)

        return max_length
        