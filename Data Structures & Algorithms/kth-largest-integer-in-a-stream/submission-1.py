class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.dui = nums
        self.k = k
        heapq.heapify(self.dui)
        while len(self.dui) > self.k:
            heapq.heappop(self.dui)

    def add(self, val: int) -> int:
        heapq.heappush(self.dui, val)
        while len(self.dui) > self.k:
            heapq.heappop(self.dui)
        return self.dui[0]
