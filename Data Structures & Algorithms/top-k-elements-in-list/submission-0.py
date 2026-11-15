class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        sort = sorted(hash.items(), key = lambda x: x[1],reverse = True)
        ans = []
        for i in range(k):
            ans.append(sort[i][0])
        return ans