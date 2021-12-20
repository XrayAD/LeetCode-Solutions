class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mid_index = int(len(matrix)/2)
        start = 0
        finish = len(matrix) - 1
        while (start <= finish):
            if matrix[mid_index][0] > target:
                finish  = mid_index - 1
                mid_index = int((start + finish)/2)
            elif matrix[mid_index][-1] < target:
                start = mid_index + 1
                mid_index = int((start + finish)/2)
            else:
                return self.searchRow(matrix[mid_index], target)
        return False

    def searchRow(self, row, target):
        mid = int(len(row) / 2)
        start = 0
        finish = len(row) - 1
        while(start <= finish):
            if row[mid] == target:
                return True
            elif row[mid] > target:
                finish = mid - 1
                mid = int((start + finish)/2)
            else:
                start = mid + 1
                mid = int((start+finish)/2)
        return False
