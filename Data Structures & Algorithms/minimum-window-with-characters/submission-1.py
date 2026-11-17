class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = {}
        for i in t:
            cnt[i] = cnt.get(i, 0) + 1
        l = 0
        start = 0
        minlen = float("inf")
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) - 1
            while all(v <= 0 for v in cnt.values()):
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    start = l
                cnt[s[l]] += 1
                l += 1
        if minlen == float("inf"):
            return ''
        return s[start : start + minlen]
