class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-i for i in nums]
        heapq.heapify(num)
        ans = []
        while k > 1:
            ans.append(num)
            heapq.heappop(num)
            k -= 1
        return -num[0]
