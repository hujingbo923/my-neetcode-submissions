class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        before, late = 0, 0
        ans = 1
        hash = set()
        for late in range(len(s)):
            while s[late] in hash:
                hash.remove(s[before])
                before += 1
            hash.add(s[late])
            ans = max(ans, late - before + 1)
        return ans
