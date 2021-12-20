class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        new = [0] * r
        for i in range(r):
            new[i] = [0] * c
        inner = 0
        outer = 0
        for i in mat:
            for j in i:
                new[inner][outer] = j
                outer += 1
                if (outer == c):
                    outer = 0
                    inner += 1
        return new
