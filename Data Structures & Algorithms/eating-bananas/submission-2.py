class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1#最小不可能是0，如果是0，l=0，r=1，mid=0就除数为0了
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
                r = mid #这里如果是-1的话就可能吧正确答案扔掉
            else:
                l = mid + 1
        return l #循环结束l==r
