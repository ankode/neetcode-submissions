class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows = len (matrix)
        cols = len (matrix[0])
        right = (rows * cols ) - 1 

        while left <= right:
            mid = left + (right - left) // 2
            if target > matrix [mid//cols][mid%cols]:
                left = mid + 1
                continue
            
            if target < matrix [mid//cols][mid%cols]:
                right = mid - 1
                continue
            
            return True
        
        return False