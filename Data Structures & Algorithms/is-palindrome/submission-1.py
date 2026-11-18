class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for i in s:
            if i >= "a" and i <= "z":
                s1.append(i.lower())
            if i >= "A" and i <= "Z":
                s1.append(i.lower())
            if i >= "0" and i <= "9":
                s1.append(i.lower())
        for i in range(len(s1) // 2):
            if s1[i] == s1[len(s1) - i - 1]:
                continue
            else:
                return False
        return True
