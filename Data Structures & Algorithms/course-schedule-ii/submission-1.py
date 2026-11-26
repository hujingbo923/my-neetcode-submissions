class Solution:
    def findOrder(self, nums: int, pre: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)
        rudu = [0] * nums
        for i in range(len(pre)):
            hashmap[pre[i][1]].append(pre[i][0])
            rudu[pre[i][0]] += 1

        q = deque(i for i in range(nums) if rudu[i] == 0)
        count = 0
        ans = []
        while q:
            temp = q.popleft()
            count += 1
            ans.append(temp)
            for i in hashmap[temp]:
                rudu[i] -= 1
                if rudu[i] == 0:
                    q.append(i)

        if count == nums:
            return ans
        else:
            return []
