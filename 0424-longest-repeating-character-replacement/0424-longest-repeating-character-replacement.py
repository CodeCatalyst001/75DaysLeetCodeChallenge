class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26  # Frequency count for A-Z
        left = 0
        max_len = 0
        max_count = 0  # Most frequent char count in current window
        
        for right in range(len(s)):
            # Add right character
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            
            # If replacements needed > k, shrink window
            replacements_needed = right - left + 1 - max_count
            while replacements_needed > k:
                left_idx = ord(s[left]) - ord('A')
                count[left_idx] -= 1
                left += 1
                # Recalculate max_count (might have changed)
                max_count = max(count)
                replacements_needed = right - left + 1 - max_count
            
            max_len = max(max_len, right - left + 1)
        
        return max_len