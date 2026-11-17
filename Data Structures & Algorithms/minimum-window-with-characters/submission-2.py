class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = {}
        for i in t:
            cnt[i] = cnt.get(i, 0) + 1 #把t出现的全加进去
        l = 0#左边
        start = 0#开头
        minlen = float("inf")
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) - 1#有一个就把cut里面的减1
            while all(v <= 0 for v in cnt.values()):#所有的v都小于等于0
                if r - l + 1 < minlen:
                    minlen = r - l + 1#记录最小值
                    start = l#记录起点
                cnt[s[l]] += 1
                l += 1
        if minlen == float("inf"):
            return ''
        return s[start : start + minlen]
