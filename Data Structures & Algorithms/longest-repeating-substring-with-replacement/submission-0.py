class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash1 = {}
        left, right = 0, 0
        ans = 0
        freq = 0
        for right in range(len(s)):
            hash1[s[right]] = hash1.get(s[right], 0) + 1
            while max(hash1.values()) < right - left + 1 - k:
                hash1[s[left]] -= 1
                left += 1
            ans = max(ans, right - left +1)
        return ans