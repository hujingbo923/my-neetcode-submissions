class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone = [-i for i in stones]
        heapq.heapify(stone)
        while len(stone) != 0 and len(stone) != 1:
            top = -heapq.heappop(stone)
            top1 = -heapq.heappop(stone)
            if top == top1:
                continue
            else:
                heapq.heappush(stone, top1 - top)  # 第一个参数是堆，第二个是加进去的新值
        if stone:
            return -stone[0]
        else:
            return 0
