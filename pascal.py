class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        new = [0] * numRows
        for i in range(numRows):
            new[i] = [1] * (i+1)
        for i in range(numRows):
            for j in range(1, i):
                new[i][j] = new[i-1][j-1] + new[i-1][j]
        return new
