class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Set all ith jth rows to zero if a 0 value is found"""
        zeros = []
        for i, arr in enumerate(matrix):
            for j, v in enumerate(arr):
                if v == 0:
                    zeros.append([i, j])
        for z in zeros:
            for i, arr in enumerate(matrix):
                for j, v in enumerate(arr):
                    if i == z[0]:
                        matrix[i] = [0 for k in arr]
                    if j == z[1]:
                        matrix[i][j] = 0
