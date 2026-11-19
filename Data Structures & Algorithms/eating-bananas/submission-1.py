class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                if piles[i] % mid == 0:
                    time += piles[i] // mid
                else:
                    time += piles[i] // mid + 1
            if time <= h:
                r = mid
            else:
                l = mid + 1
        return l
