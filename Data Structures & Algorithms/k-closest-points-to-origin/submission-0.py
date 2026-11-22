class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            temp = (x * x + y * y)
            minheap.append([temp, x, y])
        heapq.heapify(minheap)
        cnt = 0
        ans = []
        while cnt != k:
            temp1, x, y = heapq.heappop(minheap)
            ans.append([x, y])
            cnt += 1
        return ans
