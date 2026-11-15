class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seq1 = {}
        seq2 = {}
        for i in s:
            seq1[i] = seq1.get(i, 0) + 1
        for i in t:
            seq2[i] = seq2.get(i, 0) + 1
        if seq1 == seq2:
            return True
        else:
            return False