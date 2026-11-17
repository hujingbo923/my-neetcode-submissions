class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = [0] * 26
        b = [0] * 26
        left = 0
        right = len(s1) - 1
        for i in s1:
            a[ord(i) - ord("a")] += 1
        for i in s2[left : right + 1]:#初始化只和s1一样长，而且切片的时候不会取到最后，需要加1
            b[ord(i) - ord("a")] += 1
        if a == b:
            return True
        for right in range(len(s1), len(s2)):#要从lens1开始，要不然b右边会多加一次，左边会多减一次
            b[ord(s2[right]) - ord("a")] += 1
            b[ord(s2[left]) - ord("a")] -= 1
            left += 1
            if a == b:
                return True
        return False
