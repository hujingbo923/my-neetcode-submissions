class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        # 3 6 7 9
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0]==target:
                return True
            if matrix[mid][0] < target:
                l=mid+1
            if matrix[mid][0] > target:
                r=mid-1
        l1, r1 = 0, len(matrix[r])-1
        while l1<=r1:
            mid1 = (l1+r1)//2
            if matrix[r][mid1]==target:
                return True
            if matrix[r][mid1] < target:
                l1=mid1+1
            if matrix[r][mid1] > target:
                r1=mid1-1
        return False