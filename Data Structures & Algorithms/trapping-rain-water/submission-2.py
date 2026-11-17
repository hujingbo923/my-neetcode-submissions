class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lmax, rmax = 0, 0
        water = 0
        while left < right: #双指针
            if height[left] <= height[right]:#思路是找到当前位置左边和右边的最高的的较小值，小的是瓶颈，进行更新
                if height[left] > lmax:#这样其实只会收到左边限制，因为右边在if里面已经确定了
                    lmax = height[left]#不断维护边界，更高的只能作为边界，因为左边没有更高的，这里就装不上水
                else:
                    water += lmax - height[left]
                left += 1
            else:
                if height[right] > rmax:
                    rmax = height[right]
                else:
                    water += rmax - height[right]
                right -= 1
        return water        