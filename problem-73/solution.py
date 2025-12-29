class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        # Set values to null if we want to change them to zero
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                value = matrix[r][c]
                if value == 0:
                    self.clear_row_and_col(matrix=matrix, r=r, c=c)
        
        # Convert null values to zero
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                value = matrix[r][c]
                if value is None:
                    matrix[r][c] = 0

    @staticmethod
    def clear_row_and_col(matrix: list[list[int]], r: int, c: int) -> None:
        # Set non-zero values in column to null
        for i in range(len(matrix)):
            value = matrix[i][c]
            if value != 0:
                matrix[i][c] = None
        
        # Set non-zero values in row to null
        for i in range(len(matrix[0])):
            value = matrix[r][i]
            if value != 0:
                matrix[r][i] = None
