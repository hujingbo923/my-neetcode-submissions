class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in strs:
            hash.setdefault("".join(sorted(i)), []).append(i)
        return list(hash.values())